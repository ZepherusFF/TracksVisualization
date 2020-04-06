import gpxpy
import os
import pandas as pd


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
                    dict = {'Timestamp' : point.time,
                            'Latitude' : point.latitude,
                            'Longitude' : point.longitude,
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
