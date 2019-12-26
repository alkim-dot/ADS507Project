import folium
import webbrowser
import os

myMap = folium.Map(location=[45.5236, -122.6750])
myMap.save("myMap.html")

url = "file://" + os.path.realpath('myMap.hmtl')

try:
    print("[info] Opening {} in browser".format(url))
    webbrowser.open("file://" + os.path.realpath(url))
except webbrowser.Error:
    print("[info] No runnable browser found. Open {} manually.".format(url))
    print("[info] Path to heatmap file: \"{}\"".format(
        os.path.abspath(url)))



