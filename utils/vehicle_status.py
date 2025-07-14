import time

class VehicleStatus:
    def __init__(self):
        self.state_cycle = 0
        self.update_status()  # kezdeti állapot beállítása

    def update_status(self):
        cycle_map = {
            0: (True, True),    # indulás a kezdőmegállóból
            1: (True, False),   # elindult, még a zónában
            2: (False, False),
            3: (True, False),
            4: (True, True),
            5: (True, True)
        }

        self.in_stop_zone, self.stopped_at_stop = cycle_map[self.state_cycle]
        self.state_cycle = (self.state_cycle + 1) % len(cycle_map)

    def get_status(self):
        return {
            "inStopZone": self.in_stop_zone,
            "stoppedAtStop": self.stopped_at_stop
        }


if __name__== "__main__" :
    status = VehicleStatus()

    for i in range(36):  # 2 teljes ciklus
        print(f"Ciklus {i + 1}: {status.get_status()}")
        status.update_status()