import requests as req
import time
from datetime import datetime
import pandas as pd
from IPython.display import display
import Database_Connet as dc
import Article_Fliter as af
from _mysql_connector import MySQLError

# API key
API_KEY = 'VoGkNDqYbqH1htqDk3HN7b1cE9eJ3CSR'
# Search Topic
TOPIC = 'suicide depression'


def scrapeNYArticles():
    # All articles
    articles = []
    results = 1

    # A max of 10 results at a time, 10 requests per minute and 4000 requests per day
    for i in range(results):

        url = 'https://api.nytimes.com/svc/search/v2/articlesearch.json?q=' + TOPIC + '&api-key=' + API_KEY + '&page=' + str(
            i)
        response = req.get(url).json()

        # Avoid hitting APIs request limit per minute
        time.sleep(6)

        # Get necessary fields from the response
        docs = response['response']['docs']
        for doc in docs:
            pub_data = datetime.strptime(doc['pub_date'], '%Y-%m-%dT%H:%M:%S%z').strftime('%d-%m-%Y')
            filteredDoc = {'title': doc['headline']['main'], 'lead_paragraph': doc['lead_paragraph'],
                           'web_url': doc['web_url']}
            articles.append(filteredDoc)

    df = pd.DataFrame(data=articles)
    df.rename(columns={'lead_paragraph': 'body', 'Unnamed: 0': 'article_id', 'web_url': 'link'}, inplace=True)
    pd.set_option('display.max_columns', None)
    articleID = [i for i in range(1, (results * 10) + 1)]
    df.insert(0, "article_id", articleID, True)
    df.to_csv('Test_Dataset.csv', index=False)
    display(df)


def insertArticlesDB():
    nytimesData = pd.read_csv('Test_Dataset.csv')
    try:
        conn = dc.openConnection()
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            cursor.execute('DROP TABLE IF EXISTS test;')
            print('Creating table...')
            cursor.execute("CREATE TABLE test (article_id INT NOT NULL, title TEXT DEFAULT NULL, body VARCHAR(16000), link TEXT NOT NULL)")
            print("test table is created.....")
            for i, row in nytimesData.iterrows():
                if af.relatedArticles(row.loc[row.index]['title']) is True:
                    sql = "INSERT INTO nytimesdb.test VALUES (%s, %s, %s, %s)"
                    cursor.execute(sql, tuple(row))
                    print("Record inserted")
                    conn.commit()
    except MySQLError as e:
        print("Error while connecting to MySQL", e)


#scrapeNYArticles()
insertArticlesDB()
