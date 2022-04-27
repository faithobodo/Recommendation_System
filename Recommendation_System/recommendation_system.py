# -*- coding: utf-8 -*-
"""Recommendation_System.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qA4tY9t7BovCGguGBeTbFnYinbpqTSMP
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
# %matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.metrics as metrics
from sklearn.neighbors import NearestNeighbors
# from sklearn import KNeighboursClassifier

df = pd.read_csv(r"/content/ratings_Beauty.csv")
# /content/ratings_Beauty.csv
# from zipfile import ZipFile
# zip = ZipFile('/content/ratings_Beauty.csv.zip')
# zip = ZipFile('/content/ratings_Beauty.csv')
# zip.extractall()

df.head()

df.columns, df.shape,df.dtypes

df.describe()

df.Rating.unique()

sns.countplot(data=df,x=df.Rating)
plt.show()

df.dtypes

"""## Simple Popularity based Recommendation System"""

rating= pd.DataFrame(df.Rating)
top_10= rating.sort_values("Rating", ascending=False)
# print('The following products are recommended'),
top_10.head(10)
# pd.concat(df.ProductId, right_on= df.UserId)

df['Rating'].astype(int),

df.dtypes

"""## Collaborative Filtering Based Recommendation System

"""

ratings_new = Rating[Rating.ProductId.isin]

# rating_explicit = Ratin[df.Rating !=0]
# rating_implicit = df.Rating ==0
df["UserId"].unique()

rating_explicit.head()

rating_matrix = df.Rating.pivot(index="UserId", columns="ProductId", values='Rating')

def findksmilarusers(UserId, Rating, metric= any, k=any):
    similarities=[]
    indices=[]
    model_knn= NearestNeighbours(metrics=metrics, algorithm="brute")
    model_knn.fit(Rating)
    loc = Rating.index.get_loc(UserId)
    distances, indices= model_knn.kneighbours(Rating.iloc[loc,:].values.reshape(1, -1), n_neighbours= k+1), 
    similarities= 1-distances.flatten()

    return similarities, indices

def predict_itembased(UserId,ProductId, Rating, metric=any, k= any):
    prediction=wtd_sum=0
    user_loc= df.Rating.get_loc(UserId)
    product_loc= df.Rating(ProductId)
    similarities, indices= findsimilaritems(ProductId, Rating)
    sum_wt= np.sum(similarities)-1
    product=1

    for i in range(0, len(indices.flatten())):
      if indices.flatten()[i] == product_loc:
          continue;
      else:
          product= Rating.iloc[user_loc,indices.flatten()[i]] * (similarities[i])
          wtd_sum = wtd_sum + product
    prediction = int(round(wtd_sum/sum_wt))
    if prediction <=0:
        prediction = 1
    elif prediction >5:
          prediction= 5
    print("predicted rating for user {0}>>> item {1}:{2}".format(UserId,ProductId,prediction))
    return prediction

df.dtypes

prediction= predict_itembased('0205616461', df, 5.0);