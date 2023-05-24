#https://www.youtube.com/watch?v=XBYYZdpwvmc
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os

import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle 


app = Flask(__name__)
app.secret_key = '5791628bb0b13ce0c67dfde288ba245'

@app.route('/')
def index():
    return render_template("submission.html")


#turn text value into float by typecasting
@app.route('/prediction', methods=['POST', 'GET'])
def prediction():
    dep_delay = float(request.form['DepDelay'])
    unpickled_Linearmodel = pickle.load(open('linearModel.pkl', 'rb'))
    prediction = unpickled_Linearmodel.predict([[dep_delay]])
    return render_template('prediction.html', prediction = prediction[0][0])

if __name__ =='__main__':
    app.run(debug=True)

