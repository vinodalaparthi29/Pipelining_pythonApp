from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    data = pd.read_csv("data.csv")  # Load CSV
    return render_template("index.html", tables=[data.to_html(classes='data')])

if __name__ == "__main__":
    app.run(debug=True)
