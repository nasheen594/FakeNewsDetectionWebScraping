from nltk.tokenize import word_tokenize


#return matching score based on word apperance
def word_counter(query,vectorsTotal,vocab_indexed):
    tokens = word_tokenize(str(query))
    #counter to store the article id
    WordCounter = 0

    result = {}
    for aritlce in vectorsTotal:
        tempCounter = WordCounter + 1
        weight = 0
        for word in tokens:
            try:
                word_id = vocab_indexed[word]
                if vectorsTotal[WordCounter,word_id] > 0:
                    weight += 1
                    # print("word apperaed in article", tempCounter, "the word is " ,word)





            except:
                #if a word from the query doesnt exsist in the document, the weight will not change
                weight = weight
            result[tempCounter] = weight
        WordCounter = WordCounter +1
    return result



