import gpxpy
import os
import pandas as pd
import csv   
import os
import re
from datetime import timezone

#Defining Global Variables for Folder input and output
Input_Dir = 'C:/Users/Zepherus/Desktop/Strava_Activities/activities'
Output_Dir = 'C:/Users/Zepherus/Desktop/Strava_Activities/Output'

os.chdir(Input_Dir)

def parsegpx(f):
    #Parse a GPX file into a list of dictionaries.
    #Each dict is one row of the final dataset.
   
    points2 = []
    with open(f, 'r') as gpxfile:
        print(f)
        gpx = gpxpy.parse(gpxfile)
        for track in gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    timestamp = point.time.replace(tzinfo=timezone.utc).timestamp()
                    if (timestamp>1577836800):
                        dict = {
                                'Latitude' : point.latitude,
                                'Longitude' : point.longitude,
                                'Timestamp' : timestamp,
                                'Elevation' : point.elevation
                                }
                        points2.append(dict)
    return points2


files = os.listdir(Input_Dir)
df2= pd.concat([pd.DataFrame(parsegpx(f)) for f in files], keys=files)
df2.head(5)
print(df2.head(5))

os.chdir(Output_Dir)
df2.to_csv('Runs.csv')


""" 
#create csv file called merged.csv to working directory and give column names x, y & t
with open(r'Runs_othermethod.csv', 'a') as f:
    writer = csv.writer(f, quoting=csv.QUOTE_NONE, escapechar=' ', lineterminator='\n')
    writer.writerow('yxt')

os.chdir(Input_Dir)

#create a folder for your files manually
for file in os.listdir('C:/Users/Zepherus/Desktop/Strava_Activities/activities'):
    filePath =  file
    print(filePath)  
    gpx_file = open(filePath, 'r')
    gpx = gpxpy.parse(gpx_file)
    count = 0

os.chdir(Output_Dir)

#iterate through rows and append each gpx row to merged csv
for track in gpx.tracks:
    for segment in track.segments:
        for point in segment.points:
            timestamp = point.time.replace(tzinfo=timezone.utc).timestamp()
            fields=['{0},{1},{2}'.format(point.latitude, point.longitude, timestamp)] 
            #Here double whitespace is removed so QGIS accepts the time format
            re.sub(' +',' ',fields[0])
            #Graphhopper creates quite a lot of GPX points and for this purpose every second is enough.
            count += 1
            if count % 2 == 0: 
                with open(r'Runs_othermethod.csv', 'a') as f:
                    writer = csv.writer(f, quoting=csv.QUOTE_NONE, escapechar=' ', lineterminator='\n')
                    writer.writerow(fields)
 """