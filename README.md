## 📁 Projekt mappastruktúra

```
mqtt_broker_tester/
├── gtfs/                        # GTFS adatok (járatok, megállók, időpontok)
│   ├── agency.txt
│   ├── calendar.txt
│   ├── calendar_dates.txt
│   ├── feed_info.txt
│   ├── routes.txt
│   ├── shapes.txt
│   ├── stop_times.txt
│   ├── stops.txt
│   └── trips.txt
│
├── run/                         # Fő szimulációs futtató szkriptek
│   ├── __init__.py
│   ├── complete_trip_cycle.py         # Teljes járatszimuláció
│   ├── external_display_message.py    # Külső kijelző üzenet szimuláció
│   └── validator_message.py           # Jegyellenőrző rendszer szimuláció
│
├── utils/                       # Segédfüggvények és feldolgozók
│   ├── __init__.py
│   ├── get_data_from_gtfs.py         # GTFS fájlok betöltése és kezelése
│   ├── json_formatter.py             # MQTT JSON üzenetformátumok
│   ├── mqtt_message_sender.py        # MQTT kliens logika
│   ├── vehicle_status.py             # Járműállapot modellezés
│   └── __pycache__/                  # Python cache fájlok (automatikus)
│
└── README.md                   # Dokumentáció (ez a fájl)


```


## Részletes modulismertetés

### `run/` – Szimulációs szkriptek

Ezek a fájlok indítják el a különféle tesztszcenáriókat:

#### `complete_trip_cycle.py`
Ez a szkript egy teljes járat szimulációját valósítja meg egy jármű számára. 
- Beolvassa a GTFS-ből a járatok és megállók adatait.
- Az útvonal során a jármű különféle státuszokat (indulás, érkezés, mozgás) küld az MQTT brokerre.
- Cél: végigkövetni egy járat élettartamát az első indulástól az utolsó megállóig.

#### `external_display_message.py`
Ez a komponens a jármű külső kijelzőjén megjelenítendő üzeneteket szimulálja.
- Például: "72-es járat – Újpest-központ felé".
- Ezek az adatok szintén a GTFS-ből kerülnek ki (járatszám, célállomás).

#### `validator_message.py`
Jegyellenőrző rendszert szimuláló modul.
- Üzenetet küld az utas által bemutatott jegy vagy bérlet típusáról.
- Cél: tesztelni, hogy a rendszer felismeri-e az érvényes/nem érvényes utazási igazolványokat.

---

### `utils/` – Segédfüggvények és kiszolgáló logika

#### `get_data_from_gtfs.py`
A GTFS fájlok feldolgozásáért felel.
- Betölti és előkészíti az `agency.txt`, `routes.txt`, `trips.txt`, `stop_times.txt`, `stops.txt`, stb. fájlokat.
- Lekérdezéseket támogat: pl. adott járathoz tartozó megállók listázása időrendben.

#### `json_formatter.py`
Formázási segédfájl.
- Az MQTT üzenetekhez szükséges JSON struktúrákat hoz létre.
- Egységesíti a küldött adatformátumokat (pl. `vehicle_status`, `display`, `validator` típusú üzenetek).

#### `mqtt_message_sender.py`
Ez a modul küldi az MQTT üzeneteket.
- Használja a `paho.mqtt.client` könyvtárat.
- Paraméterezhető broker cím, topic, QoS, stb.
- Automatikusan újrakapcsolódik hiba esetén.

#### `vehicle_status.py`
A járművek státuszát írja le:
- Indulás, megállás, késés, aktuális pozíció.
- Ez a modul képes szimulálni egy valós időben mozgó jármű viselkedését.

---

## Kapcsolat a GTFS fájlokkal

A projekt erősen támaszkodik a GTFS fájlokra, amelyek a következő kulcsfontosságú adatokat szolgáltatják:

- **trips.txt** – Járatok azonosítói
- **stop_times.txt** – Megállási időpontok
- **stops.txt** – Megállók neve és koordinátái
- **routes.txt** – Útvonalak azonosítói és megnevezései
- **shapes.txt** – Útvonalgeometria (GPS koordináták)

A `get_data_from_gtfs.py` ezeket használja a szimulációs adatbázis felépítéséhez.

---
.


    
    
    






