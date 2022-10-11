import DBConn
import Preprocessing
import CleanText
import CalculateVector
import QueryDBActions
import pickle
import ConfigrationFile

# hold articles before cleaning and pre processing
articlesList = []

# hold articles after cleaning and before pre processing
firstStageCleaning = []
firstStagePostCleaning = []

# hold articles after pre processing
secondStageCleaning = []
secondStagePostCleaning = []

# counters for each stage that store article id
counter = 0
counter2 = 0
postCounter = 0


# retrieve links list from the database (only non scraped links)
def getArticles():
    con = DBConn.openConnection()
    cursor = con.cursor()
    query = "SELECT body FROM article where article_id"
    cursor.execute(query)
    row = cursor.fetchone()

    while row is not None:
        articlesList.append(row)
        row = cursor.fetchone()
    DBConn.closeConnection(con)


print("------- retrieving articles from database -------")
getArticles()

if ConfigrationFile.recalculate == 'Y':
    print("------- data cleaning -------")

    for x in articlesList:
        text = CleanText.textCleaning(articlesList[counter])
        firstStageCleaning.append(text)
        counter = counter + 1

    print("------- data preprocessing -------")
    for x in articlesList:
        text = Preprocessing.preProcessing(firstStageCleaning[counter2])
        secondStageCleaning.append(text)
        counter2 = counter2 + 1

    with open('secondStageCleaning.pkl', 'wb') as handle:
        pickle.dump(secondStageCleaning, handle, protocol=pickle.HIGHEST_PROTOCOL)

if ConfigrationFile.recalculate == 'N':
    print("------- data cleaning -------")
    print("------- data preprocessing -------")

    # code to load the articles pre processed from a file (to save processing time)
    with open('secondStageCleaning.pkl', 'rb') as handle:
        secondStageCleaning = pickle.load(handle)

# retrieve post and the clean and pre process them
posts = QueryDBActions.getPost()

for post in posts:
    text = CleanText.textCleaning(post[1])
    text = Preprocessing.preProcessing(text)
    cosineValue = 0
    matchingScore = 0
    wordApperanceScore = 0

    print("------- calculate score for query n.", post[0], " -------")
    sorted_cosine, matching_score_result, wordApperance = CalculateVector.startNLP(secondStageCleaning, str(text))
    for key in sorted_cosine.values():
        cosineValue = key

    for key in matching_score_result.values():
        matchingScore = key

    for key in wordApperance.values():
        wordApperanceScore = key

    appearancePercentage = (wordApperanceScore / (len(text.strip().split(" "))))

    cosine_article_id = str(list(sorted_cosine)[0])
    matching_article_id = str(list(matching_score_result)[0])
    wordApperance_article_id = str(list(wordApperance)[0])
    print("The query text is :", post[1])
    print("-------------------")
    print("cosine similarity (Angle)", sorted_cosine)
    print("link is ", QueryDBActions.getArticleLink(cosine_article_id))
    print("-------------------")
    print("matched scored (length)", matching_score_result)
    print("link is ", QueryDBActions.getArticleLink(matching_article_id))
    print("-------------------")
    print("Number of words appeared in both the qurey and the article", wordApperance, "percent of similarity ",
          appearancePercentage)
    print("link is ", QueryDBActions.getArticleLink(wordApperance_article_id))
    print("------------------------------------------------------------------------------")

    QueryDBActions.updateScore(post[0], wordApperance_article_id, appearancePercentage, cosine_article_id,
                               str(cosineValue), matching_article_id, str(matchingScore))
