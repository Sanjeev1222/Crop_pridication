import numpy as np
from flask import Flask, request, jsonify,render_template
import pickle

Flask_app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
@Flask_app.route('/')
def home():
    return render_template('index.html')
@Flask_app.route('/predict',methods=['POST'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template('index.html', prediction_text='Predicted crop is {}'.format(prediction))
if __name__ == "__main__":
    Flask_app.run(debug=True)