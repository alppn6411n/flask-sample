from flask import *
import pandas as pd
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route("/", methods = ['GET', 'POST'])
def show_tables():
    owner = request.form['ITOwner']
    owner = int(owner)
    ttype = request.form['TType']
    data = pd.read_pickle('data/data.pkl')
    sample = data[(data.ITOwner == owner) & (data.TicketType == ttype)]
    return render_template('view.html',tables=[sample.to_html(classes='sample')], titles = ['na', 'sample'])

if __name__ == "__main__":
    app.run(debug=True)
