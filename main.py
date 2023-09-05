import requests
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = "YOUR_SECRET_KEY"  # CREATE YOUR KEY
Bootstrap(app)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        response = requests.get("https://api.adviceslip.com/advice")
        advice = response.json()['slip']['advice']
        return render_template("index.html", advice=advice, encodings='utf-8')
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)