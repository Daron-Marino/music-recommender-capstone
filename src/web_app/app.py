from flask import Flask, render_template, url_for, request
import json
import requests
import datetime
import numpy as np
import pandas as pd
import base64
from io import BytesIO
import os

from  itemrec import ItemRecommender

from get_token import SpotifyAPI



app = Flask(__name__)


client = SpotifyAPI()

client.perform_authentication()

access_token = client.access_token


# instatiating the df and fitting to the recommender
artist_agg = pd.read_csv('../../spotify-data/artist_agg.csv',
                          index_col='artists')


recommender = ItemRecommender()

recommender.fit(artist_agg)



# building app
@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home(title='Music Recommender'):
  # access_token = 'BQCVX9FEUh9EmsCnI5YFDpcLev-dGU8IF0o9BRcxfD-1Vl5TgqqV8Vm30-vsyYQUNOpCNJJLfo3R37FajfDtPBtQ3iN-77ITOVRPPQJ82mGf8J-0NW_LJ2TKiq21rICOnKyvFWf8nxGlZWk'
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



