from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Sentiment Analysis route
@app.route('/sentiment_usa', methods=['GET', 'POST'])
def sentiment_usa():
    if request.method == 'POST':
        text = request.form['text']
        # Process the text and get sentiment (dummy example)
        sentiment = "Positive"  # Replace with actual sentiment analysis result
        return render_template('sentiment_result.html', sentiment=sentiment)
    return render_template('sentiment_usa.html')

# Financial Data Extraction route
@app.route('/financial', methods=['GET', 'POST'])
def financial():
    if request.method == 'POST':
        article = request.form['article']

        # Regex patterns to extract financial data
        company_pattern = r'\b([A-Z][a-zA-Z]+)\b'
        revenue_pattern = r'revenue of (\d+(?:\.\d+)?) billion'
        net_income_pattern = r'net income of (\d+(?:\.\d+)?) billion'
        eps_pattern = r'eps of (\d+(?:\.\d+)?) dollar'

        # Extract information using regex
        company_name = re.search(company_pattern, article)
        revenue = re.search(revenue_pattern, article)
        net_income = re.search(net_income_pattern, article)
        eps = re.search(eps_pattern, article)

        # Assign extracted values or default to "Not found"
        company_name = company_name.group(1) if company_name else "Not found"
        revenue = revenue.group(1) + " billion" if revenue else "Not found"
        net_income = net_income.group(1) + " billion" if net_income else "Not found"
        eps = eps.group(1) + " dollar" if eps else "Not found"

        return render_template('financial_result.html', company_name=company_name, revenue=revenue,
                               net_income=net_income, eps=eps)
    return render_template('financial.html')

# Churn Prediction route
@app.route('/churn', methods=['GET', 'POST'])
def churn():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        contract_type = request.form['contract_type']
        monthly_charges = request.form['monthly_charges']
        tenure = request.form['tenure']
        total_charges = request.form['total_charges']

        # Dummy churn prediction result (replace with actual logic)
        prediction = "Likely to Churn"  # Replace with actual churn prediction result

        return render_template('churn_result.html', customer_name=customer_name,
                               contract_type=contract_type, monthly_charges=monthly_charges,
                               tenure=tenure, total_charges=total_charges, prediction=prediction)
    return render_template('churn.html')

# Diet & Workout Recommendation route
@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        age = int(request.form['age'])
        gender = request.form['gender'].lower()
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        veg_or_nonveg = request.form['veg_or_nonveg'].lower()
        disease = request.form['disease'].lower()
        region = request.form['region'].lower()
        allergics = request.form['allergics'].lower()
        foodtype = request.form['foodtype'].lower()

        # Dummy recommendation data
        recommendations = {
            'young_male': "High-protein diet with weight lifting exercises.",
            'young_female': "Balanced diet with cardio exercises.",
            'adult_male': "Low-carb diet with moderate cardio and strength training.",
            'adult_female': "Low-fat diet with a mix of cardio and strength training.",
            # Add more categories and recommendations as needed
        }

        # Simple logic for demonstration
        if age < 30 and gender == 'male':
            recommendation = recommendations.get('young_male', "General advice: Eat healthy and exercise regularly.")
        elif age < 30 and gender == 'female':
            recommendation = recommendations.get('young_female', "General advice: Eat healthy and exercise regularly.")
        elif age >= 30 and gender == 'male':
            recommendation = recommendations.get('adult_male', "General advice: Eat healthy and exercise regularly.")
        elif age >= 30 and gender == 'female':
            recommendation = recommendations.get('adult_female', "General advice: Eat healthy and exercise regularly.")
        else:
            recommendation = "General advice: Eat healthy and exercise regularly."

        return render_template('recommend_result.html', recommendation=recommendation)

    return render_template('recommend.html')

if __name__ == '__main__':
    app.run(debug=True)
