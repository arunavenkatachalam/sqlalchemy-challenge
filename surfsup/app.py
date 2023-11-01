# Import the dependencies.
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import datetime as dt
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///surfsup/Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
# Create our session (link) from Python to the DB


#################################################
# Flask Setup
#################################################
app = Flask(__name__)



#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/station<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
        f"please enter the date in yyyy-mm-dd format"
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return the results of Precipitation Analysis"""
    # Convert the query results from your precipitation analysis   
    query_results = session.query(Measurement.date, Measurement.prcp).all()

    session.close()
    # create a dictionary to store the query results
    precipitation_query = []
    for date,prcp in query_results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["prcp"] = prcp
        precipitation_query.append(precipitation_dict)

    return jsonify(precipitation_query)


@app.route("/api/v1.0/station")
def station():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return the list of Stations from the dataset"""
    station_result = session.query(Station.station).all()
    session.close()

    # Convert list of tuples into normal list
    station_query = list(np.ravel(station_result))

    # Return a JSON list of stations from the dataset
    return jsonify(station_query)


@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)
      
    # find the recent date and calculate the start date
    Last_Year_query = session.query(Measurement.date).\
      order_by(Measurement.date.desc()).first()
    
    Start_date = dt.date(2017, 8, 23)-dt.timedelta(days =365) 
    print (Start_date)
    
    # Query the active station and store as a variable
    Most_Active_Station = session.query(Measurement.station,func.count(Measurement.station)).\
        order_by(func.count(Measurement.station).desc()).\
        group_by(Measurement.station).first()
    Most_Active_Station_id = Most_Active_Station[0]
    print(Most_Active_Station_id)
    session.close()

    """Return the dates and temperature observations of the most-active station for the previous year of data"""
    # Query the dates and temperature observations of the most-active station for the previous year of data 
    Last_year_tobs_results = session.query(Measurement.date,Measurement.station,
        Measurement.tobs).\
        filter(Measurement.station == Most_Active_Station_id).\
        filter(Measurement.date > Start_date).\
        order_by(Measurement.date).all()
    
    # create a dictionary to store the query results
    Last_year_tobs_query = []
    for date, tobs, station in Last_year_tobs_results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["station"] = station
        tobs_dict["tobs"] = tobs
        Last_year_tobs_query.append(tobs_dict)


    return jsonify(Last_year_tobs_query)

@app.route("/api/v1.0/<start>")
def start_date(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return the minimum, maximum and average of temperature with start date"""
    # Identify the minimum, maximum and average of temperature based on the start date                     
    start_date_tobs_query = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    
    session.close()

    # create a dictionary to store the query results
    start_date_tobs = []
    for min,max,avg in start_date_tobs_query:
        start_date_query = {}
        start_date_query[min] = min
        start_date_query[max] = max
        start_date_query[avg] = avg
        start_date_tobs.append(start_date_query)

    return jsonify(start_date_tobs)
   

@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return the minimum, maximum and average of temperature with start date and end date"""
    #  Identify the minimum, maximum and average of temperature based on the start date and End date
    Start_end_tobs = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).\
        filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
    
    session.close()

    # create a dictionary to store the query results
    start_end_date_tobs = []
    for min,max,avg in Start_end_tobs:
        start_end_date_query = {}
        start_end_date_query[min] = min
        start_end_date_query[max] = max
        start_end_date_query[avg] = avg
        start_end_date_tobs.append(start_end_date_query)

    return jsonify(start_end_date_tobs)


if __name__ == '__main__':
    app.run(debug=True)

