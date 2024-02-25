from flask import Flask, render_template, redirect
import psycopg2
import pandas as pd
from taipy import gui
app = Flask(__name__)

conn_str = 'postgresql://postgres:Fwc3StngKebReDyv@org-revuc-2024-inst-revuc.data-1.use1.tembo.io:5432/postgres'
try:
    # Create a new database session
    conn = psycopg2.connect(conn_str)
    print("Connected to the database")
except Exception as e:
    print(f"Unable to connect to the database: {e}")


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True)


    

def theMLPART():
    print("POOPY")