import numpy as np
from flask import Flask, request, render_template
import pickle
import os

app = Flask(__name__)

# Load model
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = pickle.load(open(model_path, "rb"))

@app.route('/')
def home():
    return render_template('index.html', prediction_text="")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        float_features = [float(x) for x in request.form.values()]
        features = [np.array(float_features)]
        prediction = model.predict(features)
        return render_template('index.html',
                               prediction_text=f'Predicted crop is {prediction[0]}')
    except Exception as e:
        return render_template('index.html',
                               prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
