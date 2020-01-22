import pandas as pd
import folium
import csv

with open('stateEsso2.csv', 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerow(["State", "NumberOfEsso"])
    writer.writerow(["0","195"])
    writer.writerow(["1","187"])
    writer.writerow(["3","23"])
    writer.writerow(["2","28"])
    writer.writerow(["8","133"])
    writer.writerow(["5","27"])
    writer.writerow(["6","110"])
    writer.writerow(["7","28"])
    writer.writerow(["4","10"])
    writer.writerow(["9","191"])
    writer.writerow(["10","13"])
    writer.writerow(["11","54"])
    writer.writerow(["13","34"])
    writer.writerow(["12","23"])
    writer.writerow(["14","35"])
    writer.writerow(["15","17"])
file.close()


