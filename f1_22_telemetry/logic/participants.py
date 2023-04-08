from f1_22_telemetry.appendices import DRIVER_IDS
from f1_22_telemetry.appendices import NATIONALITY_IDS
from f1_22_telemetry.appendices import TEAM_IDS
from f1_22_telemetry.models.participants import Driver, Drivers


def build_participants(packet) -> Drivers:
    drivers = []
    for driver in packet['participants']:
        if driver["nationality"] == 255:
            continue

        if driver["driver_id"] in DRIVER_IDS:
            driver["name"] = DRIVER_IDS[driver["driver_id"]]

        driver["nationality"] = NATIONALITY_IDS[driver["nationality"]]
        driver["team_name"] = TEAM_IDS[driver["team_id"]]

        for d in ["driver_id", "team_id"]:
            del driver[d]

        drivers.append(Driver(**driver))

    return Drivers(drivers=drivers)
