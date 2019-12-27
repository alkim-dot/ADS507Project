import folium
import webbrowser
import os
import csv
import pandas as pd
from folium.plugins import MarkerCluster
import numpy as np


myMap = folium.Map(location=[51.165691, 10.451526], zoom_start= 5)


url = "file://" + os.path.realpath('myMap.hmtl')

try:
    print("[info] Opening {} in browser".format(url))
    webbrowser.open("file://" + os.path.realpath(url))
except webbrowser.Error:
    print("[info] No runnable browser found. Open {} manually.".format(url))
    print("[info] Path to heatmap file: \"{}\"".format(
        os.path.abspath(url)))



with open('Berlin.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], popup= "<strong>Berlin</strong>", tooltip= "Berlin", icon=folium.Icon(color='green', icon='ok-sign')).add_to(myMap)

with open('Baden-Württemberg.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Baden-Württemberg', icon=folium.Icon(color='purple', icon='ok-sign')).add_to(myMap)    
  
with open('Bayern.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]],tooltip='Bayern', icon=folium.Icon(color='black', icon='remove-sign')).add_to(myMap)

with open('Brandenburg.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Brandenburg', icon=folium.Icon(color='blue', icon='remove-sign')).add_to(myMap)

with open('Hamburg.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]],  tooltip='Hamburg', icon=folium.Icon(color='red', icon='cloud')).add_to(myMap)

with open('Hessen.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Hessen', icon=folium.Icon(color='white', icon='ok-sign')).add_to(myMap)

with open('Niedersachsen.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Niedersachen', icon=folium.Icon(color='lightgray', icon='remove-sign')).add_to(myMap)

with open('Mecklenburg-Vorpommern.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Meklenburg-Vorpommern', icon=folium.Icon(color='orange', icon='cloud')).add_to(myMap)
with open('Bremen.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Bremen', icon=folium.Icon(color='white', icon='ok-sign')).add_to(myMap)       

with open('Nordrhein-Westfalen.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Nordrhein-Westfalen').add_to(myMap)

with open('Rheinland-Pfalz.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Rheinland-Pfalz', icon=folium.Icon(color='pink', icon='ok-sign')).add_to(myMap)

with open('Saarland.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Saarland', icon=folium.Icon(color='beige', icon='cloud')).add_to(myMap)

with open('Sachsen.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Sachsen', icon=folium.Icon(color='cadetblue', icon='ok-sign')).add_to(myMap)

with open('Sachsen-Anhalt.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Sachsen-Anhalt', icon=folium.Icon(color='lightblue', icon='remove-sign')).add_to(myMap)

with open('Schleswig-Holstein.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Schleswig-Holstein', icon=folium.Icon(color='darkblue', icon='cloud')).add_to(myMap)

with open('Türingen.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        folium.Marker([row[1], row[2]], tooltip='Türingen', icon=folium.Icon(color='lightred', icon='ok-sign')).add_to(myMap)

url2 = 'https://raw.githubusercontent.com/isellsoap/deutschlandGeoJSON/master/2_bundeslaender/'
state_geo = f'{url2}/1_sehr_hoch.geojson' #coordinat
state_numberesoo = 'stateEsso2.csv' #values with id 
state_data = pd.read_csv(state_numberesoo)

bins= bins = list(state_data['NumberOfEsso'].quantile([0, 0.3, 0.4, 0.8, 1]))


folium.Choropleth(
    geo_data=state_geo,
    name='choropleth',
    data=state_data,
    columns=['State', 'NumberOfEsso'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=5,
    legend_name='NumberOfEsso',
    bins = bins
).add_to(myMap)



myMap.save("myMap.html")