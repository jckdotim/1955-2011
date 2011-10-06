import os
from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/steve.js")
def js():
    return redirect(url_for('static', filename='steve.js'))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run()
