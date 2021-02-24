import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
import sys
import logging



app = Flask(__name__, template_folder='templates')
app.config['EXPLAIN_TEMPLATE_LOADING'] = True
model = pickle.load(open('rf_model2', 'rb'))



@app.route('/')
def home():
   return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
	For rendering results on HTML GUI
	'''
    print('Enter input values')
    int_features = [float(x) for x in request.form.values()]
    final_features = pd.DataFrame([int_features])
    final_features.columns=['V11','V23','V1','V22','V19','V13','V24','V10']
    prediction = model.predict_proba(final_features)
    output = prediction[0][1]
    print(output)
    if output > 0.50:
        return render_template('index.html', prediction_text='PAY ATTENTION PLEASE !!!!!! THIS TRANSACTION SEEMS FRADULENT')
    elif output <= 0.50:
        return render_template('index.html', prediction_text='EVERYTHING SEEMS OKAY... THIS TRANSACTION SEEMS NON-FRADULENT')
    else:
        return render_template('index.html', prediction_text='Please enter values to the following fields to predict whether the transaction is fradulent or not') 
     


if __name__ == "__main__":
    app.run(debug=True)
    
