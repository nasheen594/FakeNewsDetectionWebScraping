import requests
from bs4 import BeautifulSoup
import re
import DBConn
import time
import ArticleFilter

links_list = []


#retrieve links list from the database (only non scraped links)
def getLinksList():
    con = DBConn.openConnection()
    cursor = con.cursor()
    query = ("SELECT link,link_id FROM article_link where scraped ='N' and provider_id ='1'")
    cursor.execute(query)
    row = cursor.fetchone()

    while row is not None:
        links_list.append(row)
        row = cursor.fetchone()
    DBConn.closeConnection(con)

#scrape a specific link from CNN.COM
def scrapeURL (URL,link_id):
    print(URL)
    print("scraping")
    print(link_id)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    body_second_part = ""
    title = ""
    date = ""
    bodyText =""
    WholeText=""
    body_first_part_test=""

    #reorder the date
    date = URL[25:27]+'/'+ URL[28:30] + '/'+URL[20:24]

    #extract article title
    title = soup.find_all('h1', {"class": "pg-headline"})
    title = re.findall(r'>(.*?)<', str(title))

    #convert the list to text
    title = title[0]

    #for CNN.COM the article is divded into two parts.. this line scrape the first part
    body_first_part = soup.find_all('p', {"class": "zn-body__paragraph speakable"})

    #remove HTML tags
    body_first_part = re.findall(r'>(.*?)<', str(body_first_part))

    #scrape the second part
    body_second_part = soup.find_all('div', {"class": "zn-body__paragraph"})
    body_second_part = re.findall(r'>(.*?)<', str(body_second_part))

    #convert list to text and remove the first two parts of article (empty and CNN)
    for ele in body_first_part[2:]:
            body_first_part_test += ele

    #convert list to text
    for ele in body_second_part:
            bodyText += ele

    #merge the two parts
    WholeText = body_first_part[2] + bodyText

    #check if the article  related to covid
    if ArticleFilter.relatedArticles(WholeText) is True :
        print("it is related to covid")
        insertArticleDB(title, WholeText, URL, link_id)




# insert article information into database
def insertArticleDB(title, wholeText, URL,link_id):
    sql = "INSERT INTO article (title, body,link,provider_id,article_link_id) VALUES (%s, %s, %s, %s, %s)"
    val = (title, wholeText, URL, 1,link_id)
    con = DBConn.openConnection()
    cursor = con.cursor()
    cursor.execute(sql, val)
    con.commit()
    print(cursor.rowcount, "record inserted.")
    DBConn.closeConnection(con)
    updateScrapeFlag(link_id)

#scrape the links from list and sleep for 5 secs between request to avoid band
def scrapeList():
    for link in links_list:
        #send the link + link id (from the database)
        scrapeURL(link[0],link[1])
        time.sleep(3)

def updateScrapeFlag(link_id):
    sql = "UPDATE article_link set scraped = 'Y' where link_id = %s"
    val = (link_id,)
    con = DBConn.openConnection()
    cursor = con.cursor()
    cursor.execute(sql, val)
    con.commit()
    print("updated link id no " + str(link_id))
    DBConn.closeConnection(con)


getLinksList()
scrapeList()

