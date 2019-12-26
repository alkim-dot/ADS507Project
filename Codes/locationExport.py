from googleplaces import GooglePlaces, types, lang
import time, json
#import pandas as pd
import csv

query_result_next_page = None
invalid_requests_found = 0
request_count = 0

API_KEY = 'AIzaSyD_4AJz6aSbnh6u_54shNpPOVt7867FNWM'
google_places = GooglePlaces(API_KEY)

with open("essoLocations.csv", mode='w', newline='') as locationsFile:
    locationsWriter = csv.writer(locationsFile,delimiter=',')
    query = input("Search query: ")

    query_result = google_places.text_search(query)
    for place in query_result.places:
        locationsWriter.writerow([place.name, place.geo_location['lat'], place.geo_location['lng']])
        print (place.name, place.geo_location)
    morePages = True
    while True:
        time.sleep(2)
        request_count = request_count + 1
        try:
            
            if query_result.has_next_page_token:
                query_result_next_page = google_places.text_search(
                pagetoken=query_result.next_page_token)

                for place in query_result_next_page.places:
                    locationsWriter.writerow([place.name, place.geo_location['lat'], place.geo_location['lng']])
                    print (place.name, place.geo_location)
                query_result = query_result_next_page
            else:
                morePages = False
                print("end of places")
                break

        except Exception as e:
            if str(e).find('INVALID_REQUEST') != -1:
                # Maximum of 4 INVALID_REQUEST responses
                invalid_requests_found = invalid_requests_found + 1
                if invalid_requests_found > 4:
                    raise e

                #time.sleep(3)
                continue
            elif str(e).find('ZERO_RESULTS') == -1:
                raise e
            else:
                break

locationsFile.close()

    