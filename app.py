from flask import Flask, render_template, request, redirect
import requests
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators
import bokeh

app = Flask(__name__)

app.vars={}

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/init',methods='GET','POST')
def init():
  app.vars['symbol']=request.form['symbol']
  app.vars['data_type']=request.form['dat']
  return render_template('init.html',ans1='Open Value', ans2='Closing Value',ans3='Lowest Value (Daily)',ans4='Highest Value (Daily)')

@app.route('/display')
def display():
  sym=app.vars['symbol']
  dat=app.vars['data_type']
  api_key = '2WO8P8MYSVYSE8LO'
  ts = TimeSeries(api_key, output_format='pandas')
  ti = TechIndicators(api_key) 
  # Get the data, returns a tuple
# aapl_data is a pandas dataframe, aapl_meta_data is a dict
  sym_data, sym_meta_data = ts.get_daily(symbol=sym)
# aapl_sma is a dict, aapl_meta_sma also a dict
  sym_sma, sym_meta_sma = ti.get_sma(symbol=sym)
  
  if dat =='Open Value':
     dat = sym_data['1. open']
  elif dat =='Close Value':
     dat =sym_data['4. close']
  elif dat == 'Lowest Value (Daily)':
     dat = sym_data['3. low']
  else:
     dat = sym_data['2. high']       
if __name__ == '__main__':
  app.run(port=33507)
