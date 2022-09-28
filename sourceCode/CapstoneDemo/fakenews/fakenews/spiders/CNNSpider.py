from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import scrapy
from mysql.connector import (connection)
import os


import glob
import pandas as pd

# startURL = "https://www.cnn.com/health/article/sitemap-2021-8.html"
startURL = "https://www.cnn.com/politics/article/sitemap-2021-10.html"


# working
class BooksSpider(scrapy.Spider):
    name = "CNNCrawler"
    # allowed_domains = ["https://www.cnn.com/health/article/sitemap-2021-8.html"]
    # start_urls = (
    #     'https://www.cnn.com/health/article/sitemap-2021-8.html',
    # )
    allowed_domains = [startURL]
    start_urls = (
        startURL,
    )

    rules = (Rule(LinkExtractor(), callback='parse', follow=False),)

    def parse(self, response):
        for items in response.css('li'):

            if items.css('span[class=sitemap-link] a::attr(href)').extract_first():
                yield {'URL': items.css('span[class=sitemap-link] a::attr(href)').extract_first(),
                       'title': items.css('span[class=sitemap-link] a::text').extract_first()
                       # 'date':items.css('span[class=date]::text').get()

                       }

    def close(self, reason):
        csv_file = max(glob.iglob('*.csv'), key=os.path.getctime)
        dbcon = connection.MySQLConnection(user='demo', password='demo',
                                           host='127.0.0.1',
                                           database='demo')
        cursor = dbcon.cursor()
        data = pd.read_csv(csv_file)

        row_count = 0

        for i, row in data.iterrows():
            if row_count != 0:
                cursor.execute('INSERT INTO article_link(link, title,provider_id,scraped)  VALUES (%s, %s,1,"N")',
                               (row[0], row[1]))
            row_count += 1

        dbcon.commit()
        cursor.close()
        dbcon.close()

