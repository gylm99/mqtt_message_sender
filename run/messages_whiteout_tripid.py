import time
from time import sleep

from pyexpat.errors import messages

import utils.mqtt_message_sender as ms
import utils.get_data_from_gtfs as data
import utils.json_formatter  as jf
from utils.json_formatter import validator_json_format




bus_display_messages = [
        # Ünnepi / alkalmi
        "Boldog Új Évet!",
        "Kellemes Ünnepeket!",
        "Boldog Húsvétot!",
        "Boldog Anyák Napját!",
        "Boldog Nőnapot!",
        "Boldog Gyereknapot!",
        "Ünnepi Menetrend",

        # Speciális járatok
        "Próba járat",
        "Tanuló járat",
        "Tesztelés alatt",
        "Zártkörű járat",
        "Rendkívüli járat",
        "Különjárat",
        "Műszaki próba",

        # Közösségi / figyelemfelhívó
        "Köszönjük, hogy velünk utazik!",
        "Utazz velünk biztonságban!",
        "Ne feledd: jegyet érvényesíteni!",
        "Környezetbarát közlekedés",
        "Vigyázzunk egymásra!"
    ]

def external_message_whiteout_rout_number(message_number=1,  headsign=None):
    external_json=jf.external_display_json_format(message_number,"",headsign)
    ms.external_display(external_json)



def internal_message_whiteout_rout_number(message_number,headsign):
    internal_json = jf.internal_display_whiteout_route_id_json_formatter(message_number,headsign)
    ms.internal_display(internal_json)

def validator_message_whiteout_rout_number(message_number=1):
    validator_json = jf.validator_json_format(message_number, None, None, None)
    ms.validator(validator_json)

def trip_status(headsign):
    tripid_json = jf.trip_status(headsign)
    ms.trip_status(tripid_json)

def connection_status():
    connect_json = jf.connection_status(True)
    ms.connection_status(connect_json)



if __name__ == "__main__":
    message_number=1

    for headsign in bus_display_messages:
        external_message_whiteout_rout_number(message_number, headsign)
        internal_message_whiteout_rout_number(message_number,headsign)
        validator_message_whiteout_rout_number(message_number)
        trip_status(headsign)
        connection_status()
        message_number+=1
        time.sleep(20)