# from facebook_scraper import get_group_info
from facebook_scraper import get_posts
from facebook_scraper import get_profile
import pandas as pd
import re
import Credentials

list = []


def delete_html_tags(text):
   tags = re.compile('<.*?>')#regex
   return tags.sub(r'',text)


def delete_http_links(text):
    text = re.sub(r'http\S+', ' ', text)
    text = re.sub(r'bit.ly/\S+', ' ', text)
    return text

def delete_special_char(text):
    return re.sub(r'[^a-zA-z0-9.,!?/:;\"\'\s]', ' ', text)

def delete_punctuation(text):
    text = re.sub(r'([^a-zA-Z- 0-9])', ' ', text)
    return text

def delete_double_space(text):
    text = re.sub(r'    ', ' ', text)
    text = re.sub(r'   ', ' ', text)
    text = re.sub(r'  ', ' ', text)
    return text

def getPagePosts(page):
    for post in get_posts(page, credentials=(Credentials.userName, Credentials.password), pages=3):
        print("getting next post")
        list.append(str(post["text"]))


def cleanFacebookPagePost():
    df = pd.DataFrame(list, columns=['text'])
    df['text'] = df.text.apply(func=delete_http_links)
    df['text'] = df.text.apply(func=delete_special_char)
    df['text'] = df.text.apply(func=delete_punctuation)
    df['text'] = df.text.apply(func=delete_double_space)
    df.to_csv('FacebookPosts.csv')


getPagePosts("nintendo")
cleanFacebookPagePost()
















# get_group_info("latesthairstyles") # or get_group_info("latesthairstyles", cookies="cookies.txt")

# for post in get_posts(group='Excellent.Garage.Door.Service', credentials=('falsuliman2019@my.fit.edu', 'Abc$654321')):
#     print(post['text'][:50])

# print (get_profile("zuck"))


# print(get_posts(group='Excellent.Garage.Door.Service', credentials=('falsuliman2019@my.fit.edu', 'Abc$654321')))

# # print (get_group_info("french.bulldog.world"))
#
# for post in get_posts("Excellent.Garage.Door.Service", credentials=('falsuliman2019@my.fit.edu', 'Abc$654321'), comments= True):
#     print(post['text'])

# for post in get_posts("C.P.B.S.H", credentials=('falsuliman2019@my.fit.edu', 'Abc$654321'), comments=True):
#     print(post["text"])