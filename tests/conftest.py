import pytest
import json
from pathlib import Path


PWD = Path(__file__).parent


def _open_json(filename: Path):
    with open(filename, "r") as json_file:
        packet = json.load(json_file)
    return packet


@pytest.fixture
def session_data():
    return _open_json(PWD / "example_packets" / "session_data.json")


@pytest.fixture
def participants_data():
    return _open_json(PWD / "example_packets" / "participants_data.json")


@pytest.fixture
def lap_data():
    return _open_json(PWD / "example_packets" / "lap_data.json")


@pytest.fixture
def car_telemetry_data():
    return _open_json(PWD / "example_packets" / "car_telemetry_data.json")
