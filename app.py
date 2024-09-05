from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    end_date = None
    if request.method == 'POST':
        end_date = request.form['end_date']
    return render_template('index.html', end_date=end_date)

if __name__ == '__main__':
    app.run(debug=True)
