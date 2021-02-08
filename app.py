# 1. import Flask
from flask import Flask, jsonify
import pandas as pd

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

pre_df=pd.read_csv("outputs/average_prcp.csv")
pre_dict=pre_df.to_dict()

station_df=pd.read_csv("outputs/stations.csv")
station_dict=station_df.to_dict()

lastyear_df=pd.read_csv("outputs/last_year.csv")
lastyear_dict=lastyear_df.to_dict()


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"


# 4. Define what to do when a user hits the /about route
@app.route("/api/v1.0/precipitation")
def precipitation():
    print("precipitation")
    return jsonify(pre_dict)

@app.route("/api/v1.0/stations")
def stations():
    print("stations")
    return jsonify(station_dict)

@app.route("/api/v1.0/tobs")
def lastyear():
    print("stations")
    return jsonify(lastyear_dict)
   





if __name__ == "__main__":
    app.run(debug=True)