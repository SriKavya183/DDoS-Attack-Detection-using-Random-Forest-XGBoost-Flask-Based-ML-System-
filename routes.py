from flask import Blueprint, render_template, request, jsonify
from app.model import predict_ddos, FEATURES

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Extract user inputs from form fields
            input_features = {feature: float(request.form[feature]) for feature in FEATURES}
            
            # Convert values to list for model processing
            feature_values = list(input_features.values())

            # Get prediction
            prediction = predict_ddos(feature_values)

            return render_template("result.html", input_values=input_features, prediction=prediction)
        except Exception as e:
            return jsonify({"error": str(e)})

    return render_template("predict.html", features=FEATURES)


@main.route('/result')
def result():
    return render_template("result.html")
