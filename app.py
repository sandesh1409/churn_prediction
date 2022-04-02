from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__,template_folder='template')
#model = pickle.load(open('modelfile1.pkl', 'rb'))
mod = 'modelfile1.pkl'
with open(mod, 'rb') as d:
    model = pickle.load(d)
    
@app.route('/')
def home():
    return render_template('index.html')


@app.route("/predict", methods=["POST"])#,"GET"])
def predict():
    if request.method == "POST":

        signup_date = request.form.get("signup_date")
        ref_date = request.form.get("ref_date")
        money = request.form.get("money")
        time = request.form.get("time")
        country = request.form.get("country")
        
        no_of_day = ref_date - signup_date
        days = no_of_day.days
        
        int_features = [[money, time, days]]
        prediction = model.predict(int_features)
        
        
        if prediction[0] < 0.5:
            return render_template('index.html', prediction_text = 'customer will churn')
        else:
            return render_template('index.html', prediction_text = 'customer does not churn')
        

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    #app.run(debug=True)
    
        
    


    
    
