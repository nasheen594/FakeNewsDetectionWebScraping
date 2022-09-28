from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np
from num2words import num2words
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import nltk

import CleanText


# remove all stop words from the article since they have no weight
def remove_stop_words(text):
    stop_words = stopwords.words('english')
    words = word_tokenize(str(text))
    new_body = ""
    for word in words:
        if word not in stop_words and len(word) > 1:
            new_body = new_body + " " + word
    return new_body

#to lower case
def toLowerCase(text):
    return np.char.lower(text)

# THIS METHOD CONVERTS NUMBERS TO WORDS
def convert_numbers(text):
    tokens = word_tokenize(str(text))
    new_body = ""
    for word in tokens:
        try:
            word = num2words(word)
        except:
            x = 0
        new_body = new_body + " " + word
    new_body = np.char.replace(new_body, "-", " ")
    return new_body

# remove prefix and suffix
def stemming(text):
    stemmer = PorterStemmer()

    tokens = word_tokenize(str(text))
    new_body = ""
    for word in tokens:
        new_body = new_body + " " + stemmer.stem(word)
    return new_body

#return the word's root
def lemmatizing(text):
    lemmatizer = WordNetLemmatizer()

    tokens = word_tokenize(str(text))
    new_body = ""
    for word in tokens:
        new_body = new_body + " " + lemmatizer.lemmatize(word)
    return new_body

#some actions will be repeated to avoid side effects from previous  operations
def preProcessing(text):
    text = toLowerCase(text)
    text = remove_stop_words(text)
    text = convert_numbers(text)
    text = remove_stop_words(text)
    text = lemmatizing(text)
    # text = stemming(text)
    # text = convert_numbers(text)
    # text = lemmatizing(text)
    # text = stemming(text)
    return text

