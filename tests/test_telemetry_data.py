from f1_22_telemetry.logic.car import build_car_telemetry
from f1_22_telemetry.models.car import TelemetryReadings


def test_build_car_telemetry(car_telemetry_data):
    readings = build_car_telemetry(car_telemetry_data)

    assert isinstance(readings, TelemetryReadings)
