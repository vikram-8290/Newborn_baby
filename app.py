from flask import Flask
from flask import Flask, render_template, request, redirect, url_for, flash, session,app,jsonify,url_for
import numpy as np
import pandas as pd
import pickle

app=Flask(__name__)
dataset = pd.read_csv('newborn.csv')  

regmodel = pickle.load(open('regmodel.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():  
    data = request.json['data']
    output = regmodel.predict([np.array(list(data.values()))])
    return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    k = 98.2
    data = [float(x) for x in request.form.values()]
    output = regmodel.predict([np.array(data)])
    original_hemoglobin = data[2]
    post_transfusion_hemoglobin = output[0]
     # Assuming prediction is post-transfusion hemoglobin
    #Handling The Case Of Original Hemoglobin Level Is Too Low To Calculate Percentage Change
    if original_hemoglobin > 0.01:  # Adjust the threshold as needed
        prediction_percentage = abs((post_transfusion_hemoglobin - original_hemoglobin) / original_hemoglobin) * 100
        prediction_percentage = min(prediction_percentage, 98.2)
        return render_template('index.html', prediction_text='Predicted Value of Post-Hemoglobin is {:.2f}\nPredicted percentage of Post-Hemoglobin is {:.2f}% '.format(post_transfusion_hemoglobin,prediction_percentage))
    else:
        return render_template('index.html', prediction_text='Predicted Value of Post-Hemoglobin is  {:.2f}\nPredicted percentage of Post-Hemoglobin is {:.2f}% '.format(post_transfusion_hemoglobin, k))

if __name__ == "__main__":
    app.run(debug=True) 
