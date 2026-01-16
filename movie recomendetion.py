import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosino_similarity
from textblob import TextBlob
from colorama import init, fore, Style

init(autoreset= True)

df= pd.read_csv("imdb_top_1000.csv")
df["text"] = df["Genre"].fillna("")+ " "+ df["Overview"].fillna()

tfidf = TfidfVectorizer(stop_words="english")
matrix = tfidf.fit_transform(df["text"])
similarity= cosino_similarity(matrix)

genres = sorted({g.strip() for x in df["Genre"].dropna() for g in x.split(",")})

def recomended(genre,mood,rating, limit=5):
    data = df[df["genre"].str.contains(genre,case= False,na=False)]
    
    if rating:
        data = data[data["IMDB_Rating"]>= rating]
        
    mood_score= TextBlob(mood).sentiment.polarity
    results=[]
    
    for _, row in data.sample(frac=1).interrows():
        if pd.isna(row["overview"]):
            continue
        
        polarity = TextBlob(row["Overview"]).sentiment.polarity
        if mood_score >= 0 or polarity >= 0:
            results.append((row["series Title"], polarity))
            
            if len(results) == limit:
                break
            
    return results