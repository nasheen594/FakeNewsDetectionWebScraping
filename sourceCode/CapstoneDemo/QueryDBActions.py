
import DBConn



#retrieve posts from the database that doesnt have matching scores yet
def getPost():
    postList = []
    con = DBConn.openConnection()
    cursor = con.cursor()
    query = ("SELECT query_id, text FROM query where matched ='N'")
    cursor.execute(query)
    row = cursor.fetchone()

    while row is not None:
        postList.append(row)
        row = cursor.fetchone()
    DBConn.closeConnection(con)
    return postList


#update the database table with matching values and links
def updateScore(query_id, appearance_link_id, appearance_score, cosinesim_link_id, cosinesim_score, matching_link_id, matching_score):
    sql = "UPDATE query set appearance_link_id = %s , appearance_score = %s ,cosinesim_link_id = %s ,  cosinesim_score = %s , matching_link_id = %s ,  matching_score = %s, matched ='N' where query_id = %s"
    val = (appearance_link_id, appearance_score, cosinesim_link_id, cosinesim_score, matching_link_id, matching_score, query_id)
    con = DBConn.openConnection()
    cursor = con.cursor()
    cursor.execute(sql, val)
    con.commit()
    DBConn.closeConnection(con)

    # update the database table with matching values and links
# def updateScore(query_id, appearance_link_id, appearance_score, cosinesim_link_id, cosinesim_score,
#                     matching_link_id, matching_score):
#         sql = "UPDATE query set spacy_link_id = %s , spacy_score = %s ,cosinesim_link_id = %s ,  cosinesim_score = %s , matching_link_id = %s ,  matching_score = %s, matched ='N' where query_id = %s"
#         val = (
#         appearance_link_id, appearance_score, cosinesim_link_id, cosinesim_score, matching_link_id, matching_score,
#         query_id)
#         con = DBConn.openConnection()
#         cursor = con.cursor()
#         cursor.execute(sql, val)
#         con.commit()
#         DBConn.closeConnection(con)

def getArticleLink(linkId):


    articleLink = ""
    con = DBConn.openConnection()
    cursor = con.cursor()
    sql = "SELECT link FROM article where article_id = %s"
    val = (linkId,)
    cursor.execute(sql,val)
    row = cursor.fetchone()

    while row is not None:
        articleLink = row
        row = cursor.fetchone()
    DBConn.closeConnection(con)
    return articleLink


