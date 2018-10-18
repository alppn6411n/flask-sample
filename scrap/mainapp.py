import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def student():
    render_template('student.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        owner = request.form['ITOwner']
        df = pd.read_excel('WA_Fn-UseC_-IT-Help-Desk.xlsx')
        new_df = df[['ITOwner', 'ticket', 'daysOpen']].loc[df['ITOwner'] == owner]
        render_template('sample.html', tables = new_df.to_html(classes='owner'))


if __name__ == '__main__':
    app.run(debug = True, port = 5001)
