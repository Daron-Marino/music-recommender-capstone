import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

from itemrec import ItemRecommender

import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('bmh')
sns.set_palette('colorblind')
plt.rcParams.update({'font.size':15})


spotify_data = pd.read_csv('../spotify-data/data.csv')

spotify_data['artists'] = spotify_data['artists'].apply(eval).apply(' '.join)
spotify_data['release_date'] = pd.to_datetime(spotify_data['release_date'])
spotify_data['duration_min'] = (spotify_data['duration_ms']/60000).round(2)
spotify_data.drop(columns='duration_ms', inplace=True)
spotify_data.set_index('artists', inplace=True)

rec = ItemRecommender()

rec.fit(spotify_data.drop(columns=['id','name','release_date']))

print(rec.get_recommendations('Mamie Smith'))