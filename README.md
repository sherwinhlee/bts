# Bureau of Transportation Statistics - Aviation On-Time Performance
Simple Python script to automate data downloads from the USDOT's Aviation On-Time Performance database. Source data: https://www.transtats.bts.gov/Tables.asp?DB_ID=120&DB_Name=Airline%20On-Time%20Performance%20Data&DB_Short_Name=On-Time

Script as-written currently queries only the following fields:  
FL_DATE, UNIQUE_CARRIER, FL_NUM, ORIGIN_AIRPORT_ID, ORIGIN, DEST_AIRPORT_ID, DEST, CRS_DEP_TIME, DEP_TIME, DEP_DELAY, TAXI_OUT, TAXI_IN, CRS_ARR_TIME, ARR_TIME, ARR_DELAY, CARRIER_DELAY, WEATHER_DELAY, NAS_DELAY, SECURITY_DELAY, LATE_AIRCRAFT_DELAY

**Areas for code improvement**
- Generalize queried fields based on user input
- Generalize date range of query and account for new data uploads on BTS
- Clean up query string