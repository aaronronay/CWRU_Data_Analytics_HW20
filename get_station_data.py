#station data extraction

import os
import os.path
import time
import csv
import numpy
from datetime import datetime
import pandas as pd
import numpy as np
os.chdir("C:/Users/Aaron/Desktop/HW20_tableau/Citibike_Data")
new = os.getcwd().replace("\\","/")
filepaths = []
for dirpath, dirnames, filenames in os.walk(new):
    for filename in [f for f in filenames if f.endswith(".csv")]:
        filepaths.append("." + os.path.join(dirpath, filename)[len(new):].replace("\\","/"))

rowcounter = 0
station = {}
name = {}
lat = {}
lng = {}

for filename in filepaths:
    with open(filename, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        next(csvreader)
        for row in csvreader:
            rowcounter += 1
            if row[3] not in station:
                station[row[3]] = 0

            station[row[3]] += 1
            if row[3] not in name:
                name[row[3]] = row[4]
                
            if row[3] not in lat:
                if row[5] != '0.0':
                    lat[row[3]] = float(row[5])
                
            if row[3] not in lng:
                if row[6] != '0.0':
                    lng[row[3]] = float(row[6])

df = pd.DataFrame([station, name, lat, lng]).T
df.columns = ['rides', 'start_station_name', 'start_station_lat', 'start_station_lng']
df.index.name = 'start_station_id'
df.to_csv("startstations.csv")

rowcounter = 0
station = {}
name = {}
lat = {}
lng = {}

for filename in filepaths:
    with open(filename, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        next(csvreader)
        
        for row in csvreader:
            
            rowcounter += 1

            if row[7] not in station:
                station[row[7]] = 0

            station[row[7]] += 1
            
            if row[7] not in name:
                name[row[7]] = row[8]
                
            if row[7] not in lat:
                if row[9] != '0.0':
                    lat[row[7]] = float(row[9])
                
            if row[7] not in lng:
                if row[10] != '0.0':
                    lng[row[7]] = float(row[10])

df_end = pd.DataFrame([station, name, lat, lng]).T
df_end.columns = ['rides', 'end_station_name', 'end_station_lat', 'end_station_lng']
df_end.index.name = 'end_station_id'
df_end.to_csv("endstations.csv")

bikes = {}
tripduration = {}
used = {}

for filename in filepaths:
    with open(filename, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        next(csvreader)
        

        for row in csvreader:
           
            if row[11] not in bikes:
                bikes[row[11]] = 0

            bikes[row[11]] += 1
            
            if row[11] not in tripduration:
                tripduration[row[11]] = 0.0
            
            tripduration[row[11]] += float(row[0])
            
            if row[11] not in used:
                used[row[11]] = 0.0
            
            used[row[11]] += ((float(row[0]) / 3600) * 11.5)

df_miles = pd.DataFrame([bikes, tripduration, used]).T
df_miles.columns = ['times_used', 'duration', 'miles']
df_miles.index.name = 'bike_id'
df_miles.to_csv("bikes_used.csv")