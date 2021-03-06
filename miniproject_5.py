# -*- coding: utf-8 -*-
"""MiniProject 5

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eJEwIJBZWTBSZhYQYLNHfimjgsGMG-G1

Download the Dataset
Method 1
Download the Dataset from the following link:
https://www.kaggle.com/jealousleopard/goodreadsbooks/download

Reading the Dataset
Read the dataset into a Pandas Data Frame!
"""

import pandas as pd
from google.colab import files
# uploaded = files.upload()
df=pd.read_csv('books.csv')
df.head(20)

"""Popularity Based Recommender
Create a function named popularity Recommender and use it to recommend books based on popularity.
Use a weighted rank similar to that used in the IMDB rating example in lesson 2.
"""

def PopularityRecommender(df):
  #Define the minimum vote count
  minimum_vote_count = 0.75* df['ratings_count'].max()
  #Define C – the mean rating
  mean_rating = df['average_rating'].mean()

  df['weighted_rating'] = (((df['ratings_count']/(df['ratings_count']+minimum_vote_count)) * df['average_rating']) + ((minimum_vote_count/(df['ratings_count']+minimum_vote_count))*mean_rating))

  recommendations = df.sort_values(by = 'weighted_rating',ascending = False)
  return recommendations

PopularityRecommender(df)

"""Content based Recommender
Create a function named content Based Recommender and use it to recommend books based on content.

Use TF-IDF Vectorizer on the author data for each book.

Distance matrix
Choose cosine similarity for pairwise distances comparison
"""

df

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
    
def ContentBasedRecommender(title, indices, distance_matrix):
    id_ = indices[title]
    distances = list(enumerate(distance_matrix[id_]))
    distances = sorted(distances, key=lambda x: x[1].all(), reverse = True)
    distances = distances[0:10]
    recommendations = [distance[0] for distance in distances]
    print("id_", id_, "distances", distances, "recommendations", recommendations)
    return df['title'].iloc[recommendations]

tfidf = TfidfVectorizer()
df['authors'] = df['authors'].fillna('')
tfidf_matrix = tfidf.fit_transform(df['authors'])
distance_matrix = cosine_similarity(tfidf_matrix)
df1=df.drop_duplicates(subset ="title")
indices = pd.Series(df1.index, index=df1['title']).drop_duplicates()
print('Indices', indices)
ContentBasedRecommender('Harry Potter and the Half-Blood Prince (Harry Potter  #6)', indices, distance_matrix)