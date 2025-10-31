import os.path
from http.client import error

import pandas as pd
import csv
import time
import datetime as datetime

from numpy.ma.core import inner

from utils.mqtt_message_sender import external_display

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

GTFS_DIR = os.path.join(BASE_DIR,'gtfs')  # itt lehet megadni hogy melyik



# === Fájlok betöltése ===


trips_df = pd.read_csv(f"{GTFS_DIR}/trips.txt")
routes_df = pd.read_csv(f"{GTFS_DIR}/routes.txt")
stop_times_df = pd.read_csv(f"{GTFS_DIR}/stop_times.txt")
stops_df = pd.read_csv(f"{GTFS_DIR}/stops.txt")





#lekérdezi egy útvonal id alapján a hozzá tartozó route adatokat
def get_route_data_by_trip_id(trip_id)->dict:
# === 1. A trips.txt-ből kinyerjük a hozzá tartozó route_id-t ===
    trip_row = trips_df[trips_df['trip_id'] == trip_id]

    if trip_row.empty:
        print(f"Nincs ilyen trip_id: {trip_id}")
        raise
    else:
        route_id = trip_row.iloc[0]['route_id']

        # === 2. A routes.txt-ből kikeressük a route_id-t ===
        route_row = routes_df[routes_df['route_id'] == route_id]

        if route_row.empty:
            print(f"Nincs ilyen route_id: {route_id}")
        else:
            # === 3. Kiíratjuk a route adatait ===
            route_info = route_row.iloc[0]

            print(route_info['route_id'])
            print(route_info['route_short_name'])
            print(route_info['route_long_name'])
            return {"id" : route_info['route_id'],
                    "short_name": route_info['route_short_name'],
                    "long_name": route_info['route_long_name'],
                    "route_type": route_info['route_type'],
                    "color": route_info['route_color'],
                    "text_color": route_info['route_text_color'],
                    "sort_order" : route_info['route_sort_order']
                    }

# gtfs-ből meghatározza egy trip_id alapján a hozzá tartozó megálló azonosítóját és nevét és ezt egy szótárból álló listába rakja bele
def get_stops_for_trip(trip_id)->list:
    trip_stops = stop_times_df[stop_times_df['trip_id'] == trip_id].sort_values('stop_sequence')
    merged = pd.merge(trip_stops, stops_df, on='stop_id', how='left')

    stop_list = [{'id': str( row['stop_id']), 'name': row['stop_name']} for _, row in merged.iterrows()]

    return stop_list

# gtfs
def get_trip_ids()->list:
    distinct_trip_id=trips_df['trip_id'].unique()
    trip_id_list=[id for id in distinct_trip_id]
    return trip_id_list
# trip_id alapján megkeresi a hozzá tartozó trip_headsign-t
def get_trip_headsign_by_trip_id(trip_id):
    row = trips_df[trips_df['trip_id'] == trip_id]
    if not row.empty:
        return row.iloc[0]['trip_headsign']
    else:
        return f"trip_id '{trip_id}' nem található."


#megkeresi a leghosszabb trip_head_sign-al rendelkező trip_id-t.
def get_trip_id_with_longest_headsign()->str:

    longest_headsign = ""
    trip_id_with_longest = None

    for index, trip_row in trips_df.iterrows():
       if len(longest_headsign)<len(trip_row['trip_headsign']):
        longest_headsign=trip_row['trip_headsign']
        trip_id_with_longest=trip_row['trip_id']

        return trip_id_with_longest


def thury_busz_headsign_forming(trip_id)->str:
    route_data=get_route_data_by_trip_id(trip_id)
    headsign=route_data['long_name']
    return headsign

def get_all_unique_trip_headsign()->list[dict]:
    merged = pd.merge(trips_df, routes_df[['route_id', 'route_short_name']], on='route_id', how='inner')
    distinct_merged = merged[['route_short_name','trip_headsign']].drop_duplicates()
    external_display_data_list = [ {'route_number' : row['route_short_name'], 'headsign' : row['trip_headsign']} for _, row in distinct_merged.iterrows()]
    return external_display_data_list









if __name__== '__main__':
    #print(get_trip_id_with_longest_headsign())

    first_stops = stop_times_df.sort_values("stop_sequence").groupby("trip_id").first()["stop_id"]
    last_stops = stop_times_df.sort_values("stop_sequence").groupby("trip_id").last()["stop_id"]

    loop_trip_ids = first_stops[first_stops == last_stops].index.tolist()

    #for trip_id in loop_trip_ids:
     #   print(len(trip_id))

    external_display_message=get_all_unique_trip_headsign()
    for item in external_display_message:
        print(f"{item['route_number']} - {item['headsign']}")



