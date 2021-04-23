from flask import Flask, render_template, url_for, request
import json
import requests
import numpy as np
import pandas as pd
import base64
from io import BytesIO
import os

from  itemrec import ItemRecommender



app = Flask(__name__)





# instatiating the df and fitting to the recommender
artist_agg = pd.read_csv('../../spotify-data/artist_agg.csv',
                          index_col='artists')


recommender = ItemRecommender()

recommender.fit(artist_agg)

# building app
@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home(title='Music Recommender'):
  access_token = 'BQCKMdi0Lzy80an_MIhzWgAFbJ984fxw5rM-IUcab2wt8v4OBIth_-JosR1Ki9_nkv4EjAFc0Q7tk18uAep3RTLuWzc678Xz7PFQeP-6jnnZxoQ47z77vlFx8_4rTbNHqdvZ2k-F1SGp7zI'
  links = dict()
  if request.form.get('recs'):
    data1 = request.form.get('recs').split(', ')
    out = recommender.get_user_recommendation(data1)
    # links = dict()
    for item in out:
      json_url = requests.get("https://api.spotify.com/v1/search?q=" + item + '&type=artist&access_token=' + access_token)
      json_url = json_url.json()
      if len(json_url['artists']['items']) == 0:
          continue
      json_url = json_url['artists']['items'][0]['external_urls']['spotify']
      links[item] = json_url

    return render_template('home.html', title=title, recommendations=links, token=access_token)
  else:
    return render_template('home.html', title=title, alt="Try searching by your favorite artist!")

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/data-exploration')
def eda():
  return render_template('eda.html')



if __name__ == "__main__":
  app.run(debug=True)



