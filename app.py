# Import the Flask class to create the web app
# Import render_template to display HTML pages
# Import request to handle user input (eg. form data)
from flask import Flask, render_template, request
import joblib

model = joblib.load('DBS_SGD_model.pkl')

# Create a Flask application instance
# __name__ helps Flask locate files like templates and static assets

app = Flask(__name__)

# Define a route for the homepage "/"
# This route accepts both GET (page load) and POST (form submission) requests

@app.route("/", methods=["GET", "POST"])
def index():
    # When a user visits "/", Flask executes this function
    # render_template loads "index.html" from the templates/ folder
    # and returns it as the HTTP response
    return render_template("index.html")

@app.route("/main", methods=["GET", "POST"])
def main():
    return render_template("main.html")

# This block ensures the app runs only when this file is executed directly
# (and not when imported into another file)

@app.route("/dbs", methods=["GET", "POST"])
def dbs():
        return(render_template('dbs.html'))

@app.route("/dbsPrediction", methods=["GET", "POST"])
def dbsPrediction():
    q = float(request.form.get("q"))
    r = model.predict([[q]])
    r = r[0][0]
    return render_template("dbsPrediction.html", r = r)

if __name__ == "__main__":
    # Start Flask's built-in development server
    # The app will be accessible at http://127.0.0.1:5000/
    app.run()

    