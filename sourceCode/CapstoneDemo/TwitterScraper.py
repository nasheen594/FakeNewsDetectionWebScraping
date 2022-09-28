import sys

import twint
import re
import pandas as pd
import string
import nest_asyncio
nest_asyncio.apply()


def delete_html_tags(text):
   tags = re.compile('<.*?>')#regex
   return tags.sub(r'',text)

def delete_usernames(text):
    return re.sub('(@[A-Za-z]+[A-Za-z0-9-_]+)', '', text)

def delete_http_links(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'bit.ly/\S+', '', text)
    return text

def delete_special_char(text):
    return re.sub(r'[^a-zA-z0-9.,!?/:;\"\'\s]', '', text)


def delete_punctuation(text):
    text = re.sub(r'([^a-zA-Z- 0-9])', ' ', text)
    return text

def searchByUserAndTweet(user,tweetText):
    c = twint.Config()
    c.Username= user
    c.Search= tweetText
    c.Count = True
    # c.Since = '2021-07-15'
    # c.Until = '2021-09-01'
    c.Output = "Tweets.csv"
    c.Pandas = True
    c.Pandas_clean = True
    twint.run.Search(c)
    df = twint.storage.panda.Tweets_df

    cleanTweet(df)

def searchTweetByText(tweetText):
    c = twint.Config()
    c.Search= tweetText
    c.Count = True
    c.Since = '2021-07-15'
    c.Until = '2021-08-02'
    c.Output = "./Tweets_Dataset.csv"
    c.Pandas = True
    c.Pandas_clean = True
    c.Pandas_au = True
    twint.run.Search(c)
    df = twint.storage.panda.Tweets_df
    cleanTweet(df)


def searchTweetByUser(user):
    c = twint.Config()
    c.Username= user
    c.Count = True
    # c.Since = '2021-07-15'
    # c.Until = '2021-09-01'
    c.Output = "./Tweets_Dataset2.csv"
    c.Pandas = True
    c.Pandas_clean = True
    c.Pandas_au = True
    c.Store_csv = True
    c.Limit = 1000
    twint.run.Search(c)
    df = twint.storage.panda.Tweets_df
    cleanTweet(df)

def cleanTweet(df):
    if df.empty:
        print('couldnt retrieve tweets, please try again')
        sys.exit()
    df['tweet'] = df.tweet.apply(func = delete_http_links)
    df['tweet'] = df.tweet.apply(func = delete_usernames)
    df['tweet'] = df.tweet.apply(func = delete_html_tags)
    df['tweet'] = df.tweet.apply(func = delete_punctuation)

    header = ["tweet", "username", "date", "id"]
    df.to_csv('TwitterPosts.csv',  columns = header)


# searchByUserAndTweet('cnnbrk','covid')
# searchTweetByUser('cnnbrk')
searchTweetByText("COVID  LOS ANGELES INDOOR MASK")



