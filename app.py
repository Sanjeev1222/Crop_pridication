# import numpy as np
# from flask import Flask, request, jsonify,render_template
# import pickle

# app = Flask(__name__)
# model = pickle.load(open('model.pkl','rb'))
# @Flask_app.route('/')
# def home():
#     return render_template('login.html')
# @Flask_app.route('/predict',methods=['POST'])
# def predict():
#     float_features = [float(x) for x in request.form.values()]
#     features = [np.array(float_features)]
#     prediction = model.predict(features)
#     return render_template('index.html', prediction_text='Predicted crop is {}'.format(prediction))
# if __name__ == "__main__":
#     Flask_app.run(debug=True)





# import numpy as np
# from flask import Flask, request, jsonify, render_template, redirect, url_for
# import pickle

# Flask_app = Flask(__name__)

# # Load ML model
# model = pickle.load(open('model.pkl', 'rb'))

# # Hardcoded login credentials
# USERNAME = "admin@gmail.com"
# PASSWORD = "1234"

# @Flask_app.route('/')
# def home():
#     return render_template('login.html')

# # Login route
# @Flask_app.route('/login', methods=['POST'])
# def login():
#     username = request.form['username']
#     password = request.form['password']

#     if username == USERNAME and password == PASSWORD:
#         return redirect(url_for('index'))
#     else:
#         return render_template('login.html', error="Invalid Username or Password")

# # Index page (after login)
# @Flask_app.route('/index')
# def index():
#     return render_template('index.html')

# # Prediction route
# @Flask_app.route('/predict', methods=['POST'])
# def predict():
#     float_features = [float(x) for x in request.form.values()]
#     features = [np.array(float_features)]
#     prediction = model.predict(features)
#     return render_template('index.html', prediction_text=f'Predicted crop is {prediction}')

# if __name__ == "__main__":
#     Flask_app.run(debug=True)



import os
import numpy as np
from flask import Flask, request, render_template, redirect, url_for
import pickle

Flask_app = Flask(__name__)

# Load ML model with absolute path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'model.pkl')

with open(model_path, 'rb') as f:
    model = pickle.load(f)

# Store users (default one: admin)
users = {"admin": "1234"}

@Flask_app.route('/')
def home():
    return render_template('login.html')

@Flask_app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        return redirect(url_for('index'))
    else:
        return render_template('login.html', error="Invalid Username or Password")

@Flask_app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users:
            return render_template('register.html', error="Username already exists!")
        else:
            users[username] = password
            return redirect(url_for('home'))
    return render_template('register.html')

@Flask_app.route('/index')
def index():
    return render_template('index.html')

@Flask_app.route('/predict', methods=['POST'])
def predict():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)]
    prediction = model.predict(features)
    return render_template('index.html', prediction_text=f'Predicted crop is {prediction}')

if __name__ == "__main__":
    Flask_app.run(debug=True)


