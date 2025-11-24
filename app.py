from flask import Flask,request,render_template
import joblib

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    q = request.form.get("q")
    print(q)
    return(render_template("main.html"))

@app.route("/dbs",methods=["GET","POST"])
def dbs():
    return(render_template("dbs.html"))

@app.route("/dbs_prediction",methods=["GET","POST"])
def dbs_prediction():
    q = float(request.form.get("q"))
    print(q)
    model = joblib.load('dbs.pkl')
    r = model.predict([[q]])
    return(render_template("dbs_prediction.html",r=r))

@app.route("/creditability",methods=["GET","POST"])
def creditability():
    return(render_template("creditability.html"))

@app.route("/creditability_prediction",methods=["GET","POST"])
def creditability_prediction():
    q = float(request.form.get("q"))
    print(q)
    model = joblib.load('german_credit.pkl')
    r = model.predict([[q]])
    arr = ["creditable", "not creditable"]
    return(render_template("creditability_prediction.html",r=arr[r[0]]))


if __name__ == "__main__":
    app.run()