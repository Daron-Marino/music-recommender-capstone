from flask import Flask, render_template, url_for, request
import numpy as np
import pandas as pd
from io import BytesIO

# from  .. import itemrec



app = Flask(__name__)

# instatiating the df and fitting to the recommender
artist_agg = pd.read_csv('../../spotify-data/artist_agg.csv')


# recommender = itemrec.ItemRecommender()

# recommender.fit(artist_agg)


# building app
@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home(title='Music Recommender'):
  return render_template('home.html', title=title)

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/data-exploration')
def eda():
  return render_template('eda.html')



if __name__ == "__main__":
  app.run(debug=True)