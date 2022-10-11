def relatedArticles(article):
    keywords = ["depression", "suicide", "depress", "suicidal", "Depression", "Suicide", "Suicidal"]
    for word in keywords:
        if word in str(article):
            print(word)
            return True
    return False
