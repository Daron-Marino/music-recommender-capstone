from flask import Flask, render_template, url_for, request
import numpy as np
from io import BytesIO


app = Flask(__name__)

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