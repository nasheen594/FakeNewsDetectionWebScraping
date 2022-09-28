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
    query = ("SELECT link,link_id FROM article_link where scraped ='N' and provider_id ='2'")
    cursor.execute(query)
    row = cursor.fetchone()

    while row is not None:
        links_list.append(row)
        row = cursor.fetchone()
    DBConn.closeConnection(con)

def scrapeURL (URL,link_id):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    title = ""
    bodyText =""
    strong =""
    extra = ""
    contribution =""
    author_bio =""
    image_desc = ""
    copyright = ""

    #extract article title
    title = soup.find_all('h1', {"class": "headline"})
    title = re.findall(r'>(.*?)<', str(title))

    #convert the list to text
    title = title[0]

    body_first_part = soup.find_all('p')

    #remove extra parts at the start of the article
    try:
           extra = soup.find_all('span', {"class" : "dateline"})
           for i in extra:
                   body_first_part = re.sub(i.text, '', str(body_first_part))
    except:
            pass

    #remove contribution at the end of the article
    try:
        contribution = soup.find_all('i')
        contribution[:] = [x for x in contribution if not " " in x]
        contribution[:] = [x for x in contribution if not '.' in x]

        for i in contribution:
            if i.text != ".":
                body_first_part = re.sub(i.text, '', str(body_first_part))
                body_first_part = re.sub(str(i), '', str(body_first_part))

    except:
            pass

    # convert the and symbol to text
    try:
        body_first_part = re.sub('&amp;', 'and', str(body_first_part))

    except:
        pass


    # remove links to other articles.
    try:
        strong = soup.find_all('strong')
        strong[:] = [x for x in strong if not " " in x]
        strong[:] = [x for x in strong if not "" in x]
        strong[:] = [x for x in strong if not "Published" in x]
        strong[:] = [x for x in strong if not "." in x]
        for i in strong:
            body_first_part = re.sub(i.text, '', str(body_first_part))
    except:
        pass

    #remove author bio
    try:
            author_bio = soup.find_all('div', {"class" : "author-bio"})
            author_bio[:] = [x for x in author_bio if not " " in x]

            for i in author_bio:
                    body_first_part = re.sub(i.text,'',str(body_first_part))
    except:
            pass

    # remove image description
    try:
        image_desc = soup.find_all('div', {"class": "caption"})
        image_desc[:] = [x for x in image_desc if not " " in x]
        for i in image_desc:
            body_first_part = re.sub(i.text, '', str(body_first_part))

    except:
        pass

    # remove image copyright
    try:
        copyright = soup.find_all('span', {"class": "copyright"})
        copyright[:] = [x for x in copyright if not " " in x]
        for i in copyright:
            body_first_part = re.sub(i.text, '', str(body_first_part))

    except:
        pass

    #remove link to other text


    #remove HTML tags
    body_first_part = re.findall(r'>(.*?)<', str(body_first_part))

    #remove copyright text
    body_first_part = body_first_part[10:-14]

    #convert list to text
    for ele in body_first_part:
            bodyText += ele



    print(bodyText)
    #check if the article  related to covid, if so insert article into database
    if ArticleFilter.relatedArticles(bodyText) is True :
        print ("related to covid")
        insertArticleDB(title, bodyText, URL, link_id)


# insert article information into database
def insertArticleDB(title, wholeText, URL,link_id):
    sql = "INSERT INTO article (title, body,link,provider_id,article_link_id) VALUES (%s, %s, %s, %s, %s)"
    val = (title, wholeText, URL, 2,link_id)
    con = DBConn.openConnection()
    cursor = con.cursor()
    cursor.execute(sql, val)
    con.commit()
    print(cursor.rowcount, "record inserted.")
    DBConn.closeConnection(con)
    updateScrapeFlag(link_id)

#scrape the links from list and sleep for 5 secs between request to avoid getting band
def scrapeList():
    for link in links_list:
        #pass the link + link id (from the database)
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

