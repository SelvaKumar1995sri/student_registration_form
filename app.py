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

@app.route("/home", methods=['post', 'get'])
def index():
    if request.method == "POST":
        Name = request.form.get("Name")
        dob = request.form.get("Date of Birth")
        gender = request.form.get("Gender")
        country = request.form.get("Country")
        degree = request.form.get("Degree")
    else:
        user_input = {'name': Name, 'Date of Birth': dob, 'Gender': gender, 'Country':country, 'Degree':degree}
        register_collection.insert_one(user_input)
        record_data = register_collection.find_one({"_id": 0})
        return render_template('home.html')
    return render_template('home.html')

#end of code to run it
if __name__ == "__main__":
  app.run(debug=True)