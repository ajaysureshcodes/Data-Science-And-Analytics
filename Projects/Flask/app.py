from flask import Flask, render_template, request
import pickle
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
model = pickle.load(open("Random.pkl", "rb"))
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    age = int(request.form["age"])
    salary = float(request.form["salary"])
    data = [[age, salary]]
    print(data)
    prediction = model.predict(data)[0]
    if prediction == 1:
        outcome = "Likely to purchase the product"  
    else:
        outcome = "Unlikely to purchase the product"  
    return render_template("index.html", result=outcome)
if __name__ == "__main__":
    app.run(debug=True)
