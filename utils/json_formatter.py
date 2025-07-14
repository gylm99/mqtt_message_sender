import datetime



dt = datetime.datetime.now(datetime.timezone.utc)
current_datetime = dt.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"   #idő   utc formátumban


# belső kijelző kijelző mqtt json forma
def internal_display_json_format(message_number,trip_id,route_data:dict,stop_list:list,first_stop,last_stop,head_sign="Nem szállít utasokat"):
    return {
            "messageTime": current_datetime,
            "messageNumber": message_number,
            "data": {
                "trip": {
                    "id": trip_id,
                    "firstStop": first_stop,
                    "lastStop": last_stop
                },
                "route": {
                    "id": route_data['id'],
                    "shortName": route_data['short_name'],
                    "longName": route_data['long_name'],
                    "color": route_data['color'],
                    "textColor": route_data['text_color']
                },
                "headsign": head_sign,
                "departureTime": None,
                "actualStop": stop_list[0],
                "nextStops": stop_list[1:],
                "status": {
                    "inStopZone": False,
                    "stoppedAtStop": True
                }
            }
        }

#külső kijelző mqtt json forma
def external_display_json_format(message_number,route_short_name:str,head_sign="Nem szállít utasokat"):
    return {
        "messageTime" : current_datetime,
        "messageNumber": message_number,
        "data" : {
            "routeNumber": route_short_name,
            "headsign": head_sign
        }
    }

#validátor mqtt json forma
def validator_json_format(message_number,route_id:str,route_short_name:str,trip_id):
    return {
        "messageTime": current_datetime,
        "messageNumber": message_number,
        "data" : {
            "routeId": route_id,
            "routeShortName": route_short_name,
            "tripId": trip_id
        }
    }

