from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__,template_folder='template')
#model = pickle.load(open('modelfile1.pkl', 'rb'))
mod = 'modelfile.pkl'
with open(mod, 'rb') as d:
    model = pickle.load(d)
    
@app.route('/')
def home():
    return render_template('index.html')


@app.route("/predict", methods=["POST"])

def process():
    
    int_features = [x for x in request.form.values()]
        
    signup_date = pd.to_datetime(int_features[0])
    ref_date = pd.to_datetime(int_features[1])
    no_of_day = ref_date - signup_date
    day = no_of_day.days
        
    time = pd.to_numeric(int_features[2])
    money = pd.to_numeric(int_features[3])
        
        
    int_fea = np.array([[money, time, day]])
    prediction = model.predict(int_fea)
        
        
    if prediction < 0.5:
        return render_template('index.html', prediction_text = 'customer will churn')
    else:
        return render_template('index.html', prediction_text = 'customer does not churn')
    


if __name__ == "__main__":
    
    app.run(debug=True)
    
