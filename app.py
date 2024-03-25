from flask import Flask # import the Flask class from the flask module


# create an instance of Flask called app which will be the central object
app = Flask(__name__)

# Define a route
@app.route("/")
def index():
    first_name = 'Adonai'
    age = 26
    return 'Hello ' + first_name + 'who is ' + age + 'years old'