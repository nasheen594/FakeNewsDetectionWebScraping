import numpy as np
from nltk.tokenize import word_tokenize
import pandas as pd
import operator
import MatchingScore
import pickle
import ConfigrationFile

import WordApperance

cosinesDic = {}

#create a vocab of all word in articles list
def createVocab(articlesList):
    vocab = []

    for article in articlesList:
        tokens = word_tokenize(str(article))
        for word in tokens:
            if word not in vocab:
                vocab.append(word)



    # all vocab with indexs
    vocab_indexed = {}  # Dictionary to store index for each word
    index = 0
    for word in vocab:
        vocab_indexed[word] = index
        index += 1
    return vocab,vocab_indexed

#check if a word appears in a document, then store the number of documents with
def wordAppearance(articlesList, vocab):
    wordsWithCount = {}
    for word in vocab:
        wordsWithCount[word] = 0
        for article in articlesList:
            artilceSplit = article.lower().split()
            if word.lower() in artilceSplit:
                wordsWithCount[word] += 1
    return wordsWithCount


#calcuate how many times did a word appear in a single article / length of the article
def termFrequency(article, word):
    length = len(article.strip().split(" "))
    appearance = article.lower().split().count(word.lower())
    return appearance/length

def inverseDF(word, word_count, articlesCount):
    try:
        occurance = word_count[word]
    except:
        occurance = 1
        #we use a fixed vocab, and few words of the vocab might be absent in the document, in such cases, the df will be 0
        #  As we cannot divide by 0, we smoothen the value by adding 1 to the denominator.
    return np.log((articlesCount)/occurance+1)

# calculate the smooth inverse df
# def inverseDF(word, word_count, articlesCount):
#     try:
#         occurance = word_count[word]
#     except:
#         occurance = 1
#         #we use a fixed vocab and few words of the vocab might be absent in the document, in such cases, the df will be 0
#         #  As we cannot divide by 0, we smoothen the value by adding 1 to the denominator.
#     return 1 + np.log((articlesCount)/occurance+ 1)

#calculate the tf and idf and tf-idf score for each document and each word
def tf_idf(article, vocab,vocab_indexed,word_count,articlesCount):
    tf_idf_vector = np.zeros((1,len(vocab)))

    tokens = word_tokenize(str(article))
    for word in tokens:
        tf = termFrequency(article, word)
        idf = inverseDF(word,word_count,articlesCount)

        tf_idf = tf * idf
        try:
            tf_idf_vector[0,vocab_indexed[word]] = tf_idf

        except:
            pass
    return tf_idf_vector

#method that return the angle between two vectors
def cosine_similarity(a, b):
    cosine_similarity = np.dot(a, b)/(np.linalg.norm(a)*np.linalg.norm(b))
    return str(cosine_similarity[0])



def startNLP(articlesList, query):
    print("------- calculating  vocab -------")
    vocab,vocab_indexed = createVocab(articlesList)
    print("------- calculating  word count -------")

    if (ConfigrationFile.recalculate == 'Y'):
        word_count = wordAppearance(articlesList, vocab)
        # code to save the word count dic as a file (to save processing time)
        with open('wordCount.pkl', 'wb') as handle:
            pickle.dump(word_count, handle, protocol=pickle.HIGHEST_PROTOCOL)

    if (ConfigrationFile.recalculate == 'N'):

        #code to load the word count dic from a file (to save processing time)
        with open('wordCount.pkl', 'rb') as handle:
                word_count = pickle.load(handle)

    vectorsTotal = np.zeros((len(articlesList),len(vocab)))
    count = 0
    print("------- calcuating TF-IDF for each article -------")
    if (ConfigrationFile.recalculate == 'Y'):
        for article in articlesList:
            article_vector = tf_idf(article,vocab,vocab_indexed,word_count,len(articlesList))
            vectorsTotal[count,:] =article_vector
            count = count + 1

        with open('article_vector.pkl', 'wb') as handle:
            pickle.dump(vectorsTotal, handle, protocol=pickle.HIGHEST_PROTOCOL)

    if (ConfigrationFile.recalculate == 'N'):

         # code to load the articles vectors dic from a file (to save processing time)
        with open('article_vector.pkl', 'rb') as handle:
            vectorsTotal = pickle.load(handle)

    # create a vector for the query
    query_vector = tf_idf(query,vocab,vocab_indexed,word_count,len(articlesList))


    #store all vectors in pandas and csv
    allVectors = pd.DataFrame(vectorsTotal, columns=vocab_indexed.keys())
    allVectors.to_csv('df4.csv')

    print("------- calculating  cosine similarity -------")
    # claculate all cosine sim between the query and each document
    counter = 1
    for documentVector in vectorsTotal:
        cosinesDic[counter] = cosine_similarity(query_vector, documentVector)
        counter = counter + 1

    # sort cosine array by the closest match
    sorted_cosine = dict(sorted(cosinesDic.items(), key=operator.itemgetter(1), reverse=True)[:1])

    print("------- calculating  matching score -------")
    #calculate the matching score then order it by highest value
    matching_score_result = MatchingScore.matching_score(query,vectorsTotal,vocab_indexed)
    matching_score_result = dict(sorted(matching_score_result.items(), key=operator.itemgetter(1), reverse=True)[:1])

    print("------- calculating  words appearances -------")
    #calculate the similarity based on how many times words from the query appear in the article
    wordCounter = WordApperance.word_counter(query, vectorsTotal, vocab_indexed)
    wordCounter = dict(sorted(wordCounter.items(), key=operator.itemgetter(1), reverse=True)[:1])




    return sorted_cosine,matching_score_result,wordCounter


