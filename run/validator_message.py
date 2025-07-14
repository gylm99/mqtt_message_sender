import time

import utils.mqtt_message_sender as ms
import utils.get_data_from_gtfs as data
import utils.json_formatter  as jf


def all_trip():
    validator_message_number = 1

    for trip_id in trip_id_list:
        route_data = data.get_route_data_by_trip_id(trip_id)
        head_sign = data.thury_busz_headsign_forming(trip_id)
        validator_json = jf.validator_json_format(validator_message_number, route_data['id'] ,route_data['route'],trip_id)      # head_sign adatok küldése
        ms.validator(validator_json)
        time.sleep(5)
        validator_message_number += 1




if __name__ == '__main__':
    trip_id_list=[id for id in data.get_trip_ids()]



