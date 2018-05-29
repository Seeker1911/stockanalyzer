from flask import render_template
from stockanalyzer import app
from stockanalyzer.api.main import av, iex


@app.route('/')
def index():
  app.logger.warning('sample message')
  return render_template('index.html')


@app.route('/iex')
def get_iex():
  results = iex()
  return render_template('iex_api.html', results=results)


@app.route('/av')
def get_av():
  results = av()
  return render_template('av_api.html', results=results)
