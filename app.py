from flask import Flask
from flask import render_template

import psycopg2

import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/donorschoose/projects")
def donorschoose_projects():

    conn = psycopg2.connect("dbname='ashare' user='postgres' password='123456' host='localhost'")
  
    c="SELECT * FROM project limit 10000"

    df = pd.read_sql(c,conn)

    print df.head()
    return df.to_json(orient="records")


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
    print "Running on localhost - port 5000"