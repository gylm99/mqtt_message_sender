import time

import utils.mqtt_message_sender as ms
import utils.get_data_from_gtfs as data
import utils.json_formatter  as jf
from utils.mqtt_message_sender import external_display


def all_trips():
    trip_id_list = [id for id in data.get_trip_ids()]
    external_message_number = 1

    for trip_id in trip_id_list[:1]:
        route_data = data.get_route_data_by_trip_id(trip_id)
        head_sign = data.thury_busz_headsign_forming(trip_id)
        external_json = jf.external_display_json_format(external_message_number, route_data['short_name'], head_sign)
        ms.external_display(external_json)
        time.sleep(5)
        external_message_number += 1

def all_unique_trip_headsign_mqtt_message():
    data_list=data.get_all_unique_trip_headsign()
    external_message_number=1
    for external_data in data_list:
        external_json = jf.external_display_json_format(external_message_number,external_data['route_number'],external_data['headsign'])
        ms.external_display(external_json)
        time.sleep(1)
        external_message_number+=1







if __name__ == '__main__':
    #all_trips()
    all_unique_trip_headsign_mqtt_message()