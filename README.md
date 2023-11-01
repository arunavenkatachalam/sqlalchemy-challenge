# sqlalchemy challenge

Introduction
Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

PART - 1

Analyze and Explore the Climate Data

1. Use the SQLAlchemy create_engine() function to connect to your SQLite database

2. Use the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named station and measurement

3. Link Python to the database by creating a SQLAlchemy session

Precipitation Analysis

1. Find the most recent date in the dataset

2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data

3. Select only the "date" and "prcp" values

4. Load the query results into a Pandas DataFrame. Explicitly set the column names

5. Sort the DataFrame values by "date"

6. Plot the results by using the DataFrame plot method

7. Use Pandas to print the summary statistics for the precipitation data

Station Analysis

1. Design a query to calculate the total number of stations in the dataset

2. Design a query to find the most-active stations (that is, the stations that have the most rows).  List the stations and observation counts in descending order. Query the station id has the greatest number of observations

3. Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query

4. Design a query to get the previous 12 months of temperature observation (TOBS) data. 
	a) Filter by the station that has the greatest number of observations
	b) Query the previous 12 months of TOBS data for that station
	c) Plot the results as a histogram with bins=12

5. Close your session

PART - 2

Design Your Climate App

Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed. To do so, use Flask to create your routes as follows:

1. (/)

	a) Start at the homepage.

	b) List all the available routes.

2. (/api/v1.0/precipitation)

	a) Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using date as the key and prcp as the 	      value.

	b) Return the JSON representation of your dictionary.

3. (/api/v1.0/stations)

	a) Return a JSON list of stations from the dataset.

4. (/api/v1.0/tobs)

	a) Query the dates and temperature observations of the most-active station for the previous year of data.

	b) Return a JSON list of temperature observations for the previous year.

5. (/api/v1.0/<start> and /api/v1.0/<start>/<end>)

	a) Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range.

	b) For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.

	c) For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.
