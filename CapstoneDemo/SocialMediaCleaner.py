import re


def delete_html_tags(text):
   tags = re.compile('<.*?>')#regex
   return tags.sub(r'',text)

def delete_usernames(text):
    return re.sub('(@[A-Za-z]+[A-Za-z0-9-_]+)', '', text)

def delete_http_links(text):
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'bit.ly/\S+', '', text)
    return text

# def delete_numbers(text):
#     return re.sub(r'[^a-zA-z.,!?/:;\"\'\s]', '', text)

def delete_special_char(text):
    return re.sub(r'[^a-zA-z0-9.,!?/:;\"\'\s]', '', text)



