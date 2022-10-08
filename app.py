from atexit import register
from flask import Flask, render_template, request, url_for, redirect, session
import pymongo

app = Flask(__name__)
app.secret_key = "testing"
client = pymongo.MongoClient("mongodb+srv://gayathri:Sairambaba@cluster1.davwpcs.mongodb.net/?retryWrites=true&w=majority")
db = client['mydatabase']
register_collection = db['registration']

@app.route('/')
def header():
    return render_template('home.html')

@app.route("/", methods=['post', 'get'])
def index():
    if request.method == "POST":
        Name = request.form.get("Name")
        dob = request.form.get("Date of Birth")
        gender = request.form.get("Gender")
        country = request.form.get("Country")
        degree = request.form.get("Degree")
        user_found = register_collection.find_one({"Name": Name})
        if user_found:
            message = 'There already is a user by that name'
            return render_template('home.html', message=message)
        else:
            user_input = {
                'Name': Name, 
                'Date of Birth': dob, 
                'Gender': gender, 
                'Country':country, 
                'Degree':degree
                }
            register_collection.insert_one(user_input)
            record_data = register_collection.find_one({"Name": Name})
            new_reg = record_data['name']
            return render_template('home.html',data=new_reg)

    return render_template('home.html',data=new_reg)

if __name__ == "__main__":  
  app.run(debug=True)