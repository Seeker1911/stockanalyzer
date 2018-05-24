import json
from flask import render_template
from stockanalyzer import app
from stockanalyzer.api.main import main, iex


@app.route('/')
def index():
  app.logger.warning('sample message')
  results = main()
  return render_template('index.html', results=results)

@app.route('/iex')
def new():
  results = iex()
  return render_template('iex.html', results=results)
