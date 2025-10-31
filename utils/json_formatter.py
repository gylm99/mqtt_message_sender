import datetime


def _now_iso_utc_ms() -> str:
    dt = datetime.datetime.now(datetime.timezone.utc)
    return dt.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"    #idő   utc formátumban
#print(_now_iso_utc_ms())

# belső kijelző kijelző mqtt json forma
def internal_display_json_format(message_number,trip_id,route_data:dict,stop_list:list,first_stop,last_stop,head_sign="Nem szállít utasokat"):
    return {
            "messageTime": _now_iso_utc_ms(),
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
        "messageTime" : _now_iso_utc_ms(),
        "messageNumber": message_number,
        "data" : {
            "routeNumber": route_short_name,
            "headsign": head_sign
        }
    }

#validátor mqtt json forma
def validator_json_format(message_number,route_id:str,route_short_name:str,trip_id):
    return {
        "messageTime": _now_iso_utc_ms(),
        "messageNumber": message_number,
        "data" : {
            "routeId": route_id,
            "routeShortName": route_short_name,
            "tripId": trip_id
        }
    }

def internal_display_whiteout_route_id_json_formatter(message_number,headsign):
    var=    {
        "messageTime": _now_iso_utc_ms(),
        "messageNumber": message_number,
        "data": {
            "trip": None,
            "route": None,
            "headsign": headsign,
            "departureTime": None,
            "actualStop": None,
            "nextStops": None,
            "status": None
        }
    }
    return var


def connection_status(is_online:bool):
    return {"online": is_online}

def trip_status(headsign:str) ->dict:
    return {
     "tripId": None,
     "tripHeadsign": headsign,
     "routeId": None,
     "routeShortName": None,
     "stopId": None,
     "stopName": None,
     "vehicleLicensePlate": "AIGY507"
     }



if __name__ == "__main__":
    print(_now_iso_utc_ms())
