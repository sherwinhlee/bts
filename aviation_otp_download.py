"""
Appendix A - Data Download - btts_https_requests.py
Script to automate multiple 
HTTP POST requests for BTS
Aviation On-Time Performance
Database downloads.
"""
import requests
import zipfile
import io
import sys

# Extract zip file to following path
zpath = 'C:/Users/Sherwin/Desktop/BTSrawdata/'

def httprequest(url,headers,data,mo,yr):
	"""
	Function to send POST request.
	Params: request URL, request
	headers, request body, mo/yr
	of data being requested.
	"""
	s = requests.Session()
	r = s.post(url,headers=headers,data=data)
	if r.raise_for_status() is None:
		print('File response for ' + mo + ' ' + yr + ' received successfully.')
	else:
		r.raise_for_status()
	return r.content

def zip(response,path):
	"""
	Function to extract .zip
	from response to specified
	path.
	Params: response content, 
	file pathname for extraction
	location.
	"""
	z = zipfile.ZipFile(io.BytesIO(response))
	z.extractall(path)
	
def main():

	# Time period arrays
	months = ['January','February','March','April','May','June','July','August','September','October','November','December']
	months_n = range(1,13)
	years = ['2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']
	
	# Request URL
	url = 'https://www.transtats.bts.gov/DownLoad_Table.asp?Table_ID=236&Has_Group=3&Is_Zipped=0'

	# Request body
	str1 = 'UserTableName=On_Time_Performance&DBShortName=On_Time&RawDataTable=T_ONTIME&sqlstr=+SELECT+FL_DATE%2CUNIQUE_CARRIER%2CFL_NUM%2CORIGIN_AIRPORT_ID%2CORIGIN%2CDEST_AIRPORT_ID%2CDEST%2CCRS_DEP_TIME%2CDEP_TIME%2CDEP_DELAY%2CTAXI_OUT%2CTAXI_IN%2CCRS_ARR_TIME%2CARR_TIME%2CARR_DELAY%2CCARRIER_DELAY%2CWEATHER_DELAY%2CNAS_DELAY%2CSECURITY_DELAY%2CLATE_AIRCRAFT_DELAY+FROM++T_ONTIME+WHERE+Month+%3D'
	str2 = '+AND+YEAR%3D'
	str3 ='&varlist=FL_DATE%2CUNIQUE_CARRIER%2CFL_NUM%2CORIGIN_AIRPORT_ID%2CORIGIN%2CDEST_AIRPORT_ID%2CDEST%2CCRS_DEP_TIME%2CDEP_TIME%2CDEP_DELAY%2CTAXI_OUT%2CTAXI_IN%2CCRS_ARR_TIME%2CARR_TIME%2CARR_DELAY%2CCARRIER_DELAY%2CWEATHER_DELAY%2CNAS_DELAY%2CSECURITY_DELAY%2CLATE_AIRCRAFT_DELAY&grouplist=&suml=&sumRegion=&filter1=title%3D&filter2=title%3D&geo=All%A0&time='
	str4 = '&timename=Month&GEOGRAPHY=All&XYEAR='
	str5 = '&FREQUENCY='
	str6 = '&VarDesc=Year&VarType=Num&VarDesc=Quarter&VarType=Num&VarDesc=Month&VarType=Num&VarDesc=DayofMonth&VarType=Num&VarDesc=DayOfWeek&VarType=Num&VarName=FL_DATE&VarDesc=FlightDate&VarType=Char&VarName=UNIQUE_CARRIER&VarDesc=UniqueCarrier&VarType=Char&VarDesc=AirlineID&VarType=Num&VarDesc=Carrier&VarType=Char&VarDesc=TailNum&VarType=Char&VarName=FL_NUM&VarDesc=FlightNum&VarType=Char&VarName=ORIGIN_AIRPORT_ID&VarDesc=OriginAirportID&VarType=Num&VarDesc=OriginAirportSeqID&VarType=Num&VarDesc=OriginCityMarketID&VarType=Num&VarName=ORIGIN&VarDesc=Origin&VarType=Char&VarDesc=OriginCityName&VarType=Char&VarDesc=OriginState&VarType=Char&VarDesc=OriginStateFips&VarType=Char&VarDesc=OriginStateName&VarType=Char&VarDesc=OriginWac&VarType=Num&VarName=DEST_AIRPORT_ID&VarDesc=DestAirportID&VarType=Num&VarDesc=DestAirportSeqID&VarType=Num&VarDesc=DestCityMarketID&VarType=Num&VarName=DEST&VarDesc=Dest&VarType=Char&VarDesc=DestCityName&VarType=Char&VarDesc=DestState&VarType=Char&VarDesc=DestStateFips&VarType=Char&VarDesc=DestStateName&VarType=Char&VarDesc=DestWac&VarType=Num&VarName=CRS_DEP_TIME&VarDesc=CRSDepTime&VarType=Char&VarName=DEP_TIME&VarDesc=DepTime&VarType=Char&VarName=DEP_DELAY&VarDesc=DepDelay&VarType=Num&VarDesc=DepDelayMinutes&VarType=Num&VarDesc=DepDel15&VarType=Num&VarDesc=DepartureDelayGroups&VarType=Num&VarDesc=DepTimeBlk&VarType=Char&VarName=TAXI_OUT&VarDesc=TaxiOut&VarType=Num&VarDesc=WheelsOff&VarType=Char&VarDesc=WheelsOn&VarType=Char&VarName=TAXI_IN&VarDesc=TaxiIn&VarType=Num&VarName=CRS_ARR_TIME&VarDesc=CRSArrTime&VarType=Char&VarName=ARR_TIME&VarDesc=ArrTime&VarType=Char&VarName=ARR_DELAY&VarDesc=ArrDelay&VarType=Num&VarDesc=ArrDelayMinutes&VarType=Num&VarDesc=ArrDel15&VarType=Num&VarDesc=ArrivalDelayGroups&VarType=Num&VarDesc=ArrTimeBlk&VarType=Char&VarDesc=Cancelled&VarType=Num&VarDesc=CancellationCode&VarType=Char&VarDesc=Diverted&VarType=Num&VarDesc=CRSElapsedTime&VarType=Num&VarDesc=ActualElapsedTime&VarType=Num&VarDesc=AirTime&VarType=Num&VarDesc=Flights&VarType=Num&VarDesc=Distance&VarType=Num&VarDesc=DistanceGroup&VarType=Num&VarName=CARRIER_DELAY&VarDesc=CarrierDelay&VarType=Num&VarName=WEATHER_DELAY&VarDesc=WeatherDelay&VarType=Num&VarName=NAS_DELAY&VarDesc=NASDelay&VarType=Num&VarName=SECURITY_DELAY&VarDesc=SecurityDelay&VarType=Num&VarName=LATE_AIRCRAFT_DELAY&VarDesc=LateAircraftDelay&VarType=Num&VarDesc=FirstDepTime&VarType=Char&VarDesc=TotalAddGTime&VarType=Num&VarDesc=LongestAddGTime&VarType=Num&VarDesc=DivAirportLandings&VarType=Num&VarDesc=DivReachedDest&VarType=Num&VarDesc=DivActualElapsedTime&VarType=Num&VarDesc=DivArrDelay&VarType=Num&VarDesc=DivDistance&VarType=Num&VarDesc=Div1Airport&VarType=Char&VarDesc=Div1AirportID&VarType=Num&VarDesc=Div1AirportSeqID&VarType=Num&VarDesc=Div1WheelsOn&VarType=Char&VarDesc=Div1TotalGTime&VarType=Num&VarDesc=Div1LongestGTime&VarType=Num&VarDesc=Div1WheelsOff&VarType=Char&VarDesc=Div1TailNum&VarType=Char&VarDesc=Div2Airport&VarType=Char&VarDesc=Div2AirportID&VarType=Num&VarDesc=Div2AirportSeqID&VarType=Num&VarDesc=Div2WheelsOn&VarType=Char&VarDesc=Div2TotalGTime&VarType=Num&VarDesc=Div2LongestGTime&VarType=Num&VarDesc=Div2WheelsOff&VarType=Char&VarDesc=Div2TailNum&VarType=Char&VarDesc=Div3Airport&VarType=Char&VarDesc=Div3AirportID&VarType=Num&VarDesc=Div3AirportSeqID&VarType=Num&VarDesc=Div3WheelsOn&VarType=Char&VarDesc=Div3TotalGTime&VarType=Num&VarDesc=Div3LongestGTime&VarType=Num&VarDesc=Div3WheelsOff&VarType=Char&VarDesc=Div3TailNum&VarType=Char&VarDesc=Div4Airport&VarType=Char&VarDesc=Div4AirportID&VarType=Num&VarDesc=Div4AirportSeqID&VarType=Num&VarDesc=Div4WheelsOn&VarType=Char&VarDesc=Div4TotalGTime&VarType=Num&VarDesc=Div4LongestGTime&VarType=Num&VarDesc=Div4WheelsOff&VarType=Char&VarDesc=Div4TailNum&VarType=Char&VarDesc=Div5Airport&VarType=Char&VarDesc=Div5AirportID&VarType=Num&VarDesc=Div5AirportSeqID&VarType=Num&VarDesc=Div5WheelsOn&VarType=Char&VarDesc=Div5TotalGTime&VarType=Num&VarDesc=Div5LongestGTime&VarType=Num&VarDesc=Div5WheelsOff&VarType=Char&VarDesc=Div5TailNum&VarType=Char'

	# Request headers
	headers = {
		'Content-Type':'application/x-www-form-urlencoded',
		'Host':'www.transtats.bts.gov',
		'Referer':'https://www.transtats.bts.gov/DL_SelectFields.asp'
		}
	
	# Send HTTP request via POST
	print("Sending HTTP request...")
	for y in years:
		if y == '2003':
		# Half-year loop for introduction of delay data in June 2003
			for m in months_n[5:12]:
				data = str1 + str(m) + str2 + y + str3 + months[m-1] + str4 + y + str5 + str(m) + str6
				content = httprequest(url,headers,data,months[m-1],y)
				zip(content,zpath)
		elif y == '2017':
		# Partial-year loop for data up through September 2017
			for m in months_n[:9]:
				data = str1 + str(m) + str2 + y + str3 + months[m-1] + str4 + y + str5 + str(m) + str6
				content = httprequest(url,headers,data,months[m-1],y)
				zip(content,zpath)		
		else:
		# Full-year loop for all other years
			for m in months_n:
				data = str1 + str(m) + str2 + y + str3 + months[m-1] + str4 + y + str5 + str(m) + str6
				content = httprequest(url,headers,data,months[m-1],y)
				zip(content,zpath)	
				
# call function
if __name__ == '__main__':
	main()