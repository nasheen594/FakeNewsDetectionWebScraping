

def relatedArticles(article):
    keywords = ["COVID", "COVID19", "COVID-19", "CORONA",  "Coronavirus", "Ventilator", "Novel strain" , "Social distancing" ,
                 "Self-quarantine" , "Outbreak" , "Pandemic" , "Herd immunity" , "CDC" , "VACCINATION" , "vaccine" , "PFIZER" ,
                 "Moderna" , "Johnson" , "Antibodies" , "quarantine" , "SARS2" , "ANTIVIRAL" , "MERS" ,
                 "Centers for Disease Control and Prevention", "vaccinated"]
    for word in keywords:
        if word in article:
            print(word)
            return True
    return False
