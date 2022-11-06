import re

def delete_html_tags(text):
   tags = re.compile('<.*?>')#regex
   return tags.sub(r'',text)

def delete_usernames(text):
    return re.sub('(@[A-Za-z]+[A-Za-z0-9-_]+)', ' ', text)

def delete_http_links(text):
    text = re.sub(r'http\S+', ' ', text)
    text = re.sub(r'bit.ly/\S+', ' ', text)
    return text

def delete_special_char(text):
    # return re.sub(r'[^a-zA-z0-9.,!?/:;\"\'\s]', ' ', str(text))
    return re.sub(r'[^a-zA-z0-9,!?/:;\"\'\s]', ' ', str(text))


def delete_punctuation(text):
    # text = re.sub(r'([^a-zA-Z- 0-9])', ' ', str(text))
    text = re.sub('[^\w.]+', ' ', str(text))
    text = re.sub(r'(?<!\d)[.,;:](?!\d)', ' ', str(text))

    return text

def delete_double_space(text):
    text = re.sub(r'    ', ' ', str(text))
    text = re.sub(r'   ', ' ', str(text))
    text = re.sub(r'  ', ' ', str(text))
    return text

def delete_xa0(text):
    text = re.sub(r'(xa0)', ' ', str(text))
    return text

def removeCommaFromNumbers(text):
    text = re.sub(r'(\d+),(\d+)', r'\1\2', str(text))
    return text


def removeCommaS(text):
    text = re.sub("'s", ' ', str(text))
    return text
# def removePunctioations(text):
#     text = re.sub('[^\d.]+', ' ', str(text))
#     return text



def textCleaning (text):
    text = removeCommaFromNumbers(text)
    text = delete_punctuation(text)
    text = delete_xa0(text)
    # text = removeCommaS(text)
    text = delete_double_space(text)
    # text = delete_special_char(text)
    # text = delete_double_space(text)

    return text