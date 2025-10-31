import os
import time

from utils import get_data_from_gtfs as data, json_formatter as jf, mqtt_message_sender as ms

#egy gtfs alapján végig megy az összes trip_id-n és elküldi mqtt-n a hozzá tartozó adatokat a megfelelő csatornákon.
if __name__ == "__main__":
    #print(f"Current working directory: {os.getcwd()}")
    trip_id_list=[]

    #trip_id_list.append(data.get_trip_ids())
    #trip_id_list.append(data.get_trip_id_with_longest_headsign())
    #trip_id_list.append('32-2010-tansz-1')
    trip_id_list=data.get_trip_ids()   #összes aznosító

    external_message_number=1
    validator_message_number=1
    internal_message_number = 1


    for trip_id in trip_id_list[50:]:
        route_data=data.get_route_data_by_trip_id(trip_id)  #egy útvonal adatai adatai egy trip_id alapján
        stop_list=data.get_stops_for_trip(trip_id)  #egy járathoz tardozó megállók {{azonosító},{név}}  trip_id alapján
        head_sign=data.get_trip_headsign_by_trip_id(trip_id) #egy járathoz tartozó fő kijelző szöveg adat

        external_display_json=jf.external_display_json_format(external_message_number, route_data['short_name'], head_sign)  #külső kijelzőre json formázás
        validator_json=jf.validator_json_format(validator_message_number, route_data['id'] ,route_data['short_name'], trip_id) #validátorra json formázás

        ms.external_display(external_display_json)  # validátorra küld adatot
        ms.validator(validator_json) #a külső kijelzőkre küld adatot

        first_stop=stop_list[0]
        last_stop=stop_list[-1]

        #végig megy egy trip_id hoz tartozó megállókon és elküldi a lista elemét a belső kijelzőre. Minden ciklus végén kiveszi a listából a legelső elemet.
        # Ezzel jelezzük hogy elhagytuk a megállót.
        while stop_list:
            internal_message=jf.internal_display_json_format(internal_message_number, trip_id, route_data, stop_list, first_stop, last_stop,head_sign=head_sign) # belső kijelzőre json formázás
            ms.internal_display(internal_message)  #üzenet küldés belső kijelzőre
            stop_list.pop(0)  #a megállók listából kiveszi a legelső elemet
            internal_message_number+=1
            time.sleep(20)   #belső üzenetek közötti idő
        external_message_number+=1

        validator_message_number+=1