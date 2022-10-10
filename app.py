from atexit import register
from re import fullmatch
from webbrowser import get
from flask import Flask, render_template, request, url_for, redirect, session
import pymongo

app = Flask(__name__)
client = pymongo.MongoClient("mongodb+srv://gayathri:Sairambaba@cluster1.davwpcs.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database('mydatabase')
records = db.registry

@app.route("/", methods=['post', 'get'])
def index():
    
    if request.method == "POST":
        name = request.form.get("fullname")
        dob = request.form.get("dob")
        gender = request.form.get("gender")
        country = request.form.get("city")
        degree = request.form.get("degree")
        data = {'fullname':name, 'dob':dob, 'gender':gender, 'Country':country, 'degree':degree}
        records.insert_one(data)
        return render_template('result.html')

    return render_template('index.html')

if __name__ == "__main__":  
  app.run(debug=True)