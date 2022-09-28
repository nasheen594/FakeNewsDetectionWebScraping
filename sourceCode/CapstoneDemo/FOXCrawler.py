import bs4 as bs
import urllib.request
import re
import DBConn


extracted_url=""
title= ""
provider = 2
scrapped = 'N'



#insert the extracted data to DB
def insertLinksDB(title, provider, extracted_url,scrapped):
    sql = "INSERT INTO article_link (provider_id,link,title,scraped) VALUES (%s, %s, %s, %s)"
    val = (provider, extracted_url, title, scrapped)
    con = DBConn.openConnection()
    cursor = con.cursor()
    cursor.execute(sql, val)
    con.commit()
    print("record inserted. title: " + str(title))
    DBConn.closeConnection(con)

# read the xml page the contains the links
sauce = urllib.request.urlopen('https://www.foxnews.com/sitemap.xml?type=articles&from=1626389015000').read()
soup = bs.BeautifulSoup(sauce,'xml')

# find element 'loc' on the xml file, which contains the URLS and extract the link
# also extract links that are in health section
#then extract the title from the link
for url in soup.find_all('loc'):
    category = 'health'
    # category = 'us'
    length = 24 + len(category)
    if ((url.text[24:length]) == category):

        extracted_url = url.text
        title = re.sub('-',' ',url.text[31:])
        insertLinksDB(title, provider, extracted_url, scrapped)
        extracted_url = ""
        title = ""









