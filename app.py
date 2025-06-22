from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load and clean the dataset
data = pd.read_csv('scheme_data.csv')
data.columns = data.columns.str.strip()  # Remove leading/trailing spaces

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    age = int(request.form['age'])
    gender = request.form['gender']
    income_input = int(request.form['income'])  # Income entered by user
    occupation = request.form['occupation']
    region = request.form['region']  # Optional for now

    # Map income amount to range category
    if income_input < 20000:
        income_level = 'Low'
    elif income_input < 50000:
        income_level = 'Medium'
    else:
        income_level = 'High'

    # Filter schemes based on eligibility
    filtered = data[
        (data['Min_Age'] <= age) &
        (data['Max_Age'] >= age) &
        ((data['Gender'] == gender) | (data['Gender'] == 'Any')) &
        ((data['Income_Range'] == income_level) | (data['Income_Range'] == 'Any')) &
        ((data['Occupation'] == occupation) | (data['Occupation'] == 'Any'))
    ]

    return render_template('result.html', schemes=filtered.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
