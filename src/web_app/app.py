from flask import Flask, render_template, url_for, request
import numpy as np
import pandas as pd
import base64
from io import BytesIO

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
  if request.form.get('recs'):
    data1 = request.form.get('recs').split(', ')
    out = recommender.get_user_recommendation(data1)
    return render_template('home.html', title=title, recommendations=out)
  else:
    return render_template('home.html', title=title, alt="Try searching by your favorite artist!")
   # recommendations=f'Your recommendations are {out}'

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/data-exploration')
def eda():
  return render_template('eda.html')

# @app.route('/get-recommendations')
# def recs():
#   return render_template('recs.html')


if __name__ == "__main__":
  app.run(debug=True)

