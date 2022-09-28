from nltk.tokenize import word_tokenize


#return matching score based on word apperance
def matching_score(query,vectorsTotal,vocab_indexed):
    tokens = word_tokenize(str(query))
    #counter to store the article id
    matchingScoreCounter = 0
    result = {}
    for aritlce in vectorsTotal:
        tempCounter = matchingScoreCounter + 1
        weight = 0
        for word in tokens:
            try:
                word_id = vocab_indexed[word]
                if vectorsTotal[matchingScoreCounter,word_id] > 0:
                    weight += vectorsTotal[matchingScoreCounter,word_id]

            except:
                #if a word from the query doesnt exsist in the document, the weight will not change
                weight = weight
            result[tempCounter] = weight
        matchingScoreCounter = matchingScoreCounter +1
    return result



