
import datetime as dt
import numpy as np
import pandas as pd
#Now let's get the dependencies we need for SQLAlchemy, Add the SQLAlchemy dependencies after the other dependencies you already imported in app.py
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
#Finally, add the code to import the dependencies that we need for Flask. You'll import these right after your SQLAlchemy dependencies.\n",
from flask import Flask, jsonify
#Set Up the Database\n",
#The create_engine() function allows us to access and query our SQLite database file
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
# we're going to reflect our tables using Python Flask function
Base.prepare(engine, reflect=True)
# With the database reflected, we can save our references to each table. Again, they'll be the same references as the ones we wrote earlier in this module. We'll create a variable for each of the classes so that we can reference them later, as shown below\n",
Measurement = Base.classes.measurement
Station = Base.classes.station
# create a session link from Python to our database with the following code
session = Session(engine)
#Set Up Flask 
#Ask David

#Create the Welcome Route\n",
app = Flask(__name__)
@app.route("/")
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:<br/>
    /api/v1.0/precipitation<br/>
    /api/v1.0/stations<br/>
    /api/v1.0/tobs<br/>
    /api/v1.0/temp/start/end<br/>
    ''')
# Flask Run



# Next, we will create the precipitation() function
#First, we want to add the line of code that calculates the date one year ago from the most recent date in the database
#def precipitation():
#  #   prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
#   # precipitation = session.query(Measurement.date, Measurement.prcp).\
#       filter(Measurement.date >= prev_year).all()
#    return

# We'll use jsonify() to format our results into a JSON structured file. When we run this code, we'll see what the JSON file structure looks like. Here's an example of what a JSON file might look like:\n",
# {
# \"city\" : {
# \"name\" : \"des moines\"
#         \"region\" : \"midwest\
# }
@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
     filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    return jsonify(stations=stations)    
@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
      filter(Measurement.station == 'USC00519281').\
      filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    return jsonify(temps=temps)
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start="2017-06-01", end="2017-06-30"):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    return jsonify(temps)
if __name__=="__main__":
   app.run()