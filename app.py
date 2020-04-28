# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GQlSIqbbkYL5BFy5K2N4smRTHhCA11YW
"""

from flask import Flask,render_template,request,jsonify
import pickle
import numpy as np
app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
  int_features = [int(x) for x in request.form.values()]
  final_features = [np.array(int_features)]
  prediction = model.predict(final_features)
  output = round(prediction[0], 2)
  if (output>=0.5):
    return render_template('result.html',pred='The chances of his leaving are {} %'.format(output))

  else:
    return render_template('result1.html',pred=' ')


if __name__=='__main__':
  app.run(debug=True)

