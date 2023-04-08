from f1_22_telemetry.logic.participants import build_participants
from f1_22_telemetry.models.participants import Drivers


def test_build_participants(participants_data):
    drivers = build_participants(participants_data)
    assert isinstance(drivers, Drivers)
    assert len(drivers.drivers) == 20
