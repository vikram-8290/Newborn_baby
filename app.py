from flask import Flask
from flask import Flask, render_template, request, redirect, url_for, flash, session,app,jsonify,url_for
import numpy as np
import pandas as pd
import pickle

app=Flask(__name__)

regmodel = pickle.load(open('regmodel.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():  
    data = request.json['data']
    output = regmodel.predict([np.array(list(data.values()))])
    return jsonify(output[0])

if __name__ == "__main__":
    app.run(debug=True) 
