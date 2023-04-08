from f1_22_telemetry.models.car import CarTelemetryReading
from f1_22_telemetry.models.car import TelemetryReadings


def build_car_telemetry(packet) -> TelemetryReadings:
    readings = []

    for reading in packet['car_telemetry_data']:
        readings.append(CarTelemetryReading(**reading))

    return TelemetryReadings(car_telemetry_data=readings)
