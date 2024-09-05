from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Function to calculate the difference between two dates
def countdown(target_date):
    today = datetime.now().date()
    target = datetime.strptime(target_date, '%Y-%m-%d').date()
    delta = target - today
    return delta.days

# Route to handle the web page and form submission
@app.route('/', methods=['GET', 'POST'])
def home():
    days_remaining = None
    end_date = None  # Initialize end_date to avoid UnboundLocalError
    if request.method == 'POST':
        end_date = request.form['end_date']
        days_remaining = countdown(end_date)
    return render_template('index.html', days_remaining=days_remaining, end_date=end_date)

if __name__ == '__main__':
    app.run(debug=True)
