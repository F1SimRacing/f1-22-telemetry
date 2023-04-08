from typing import List

from pydantic import BaseModel


class CarTelemetryReading(BaseModel):
    brake: float
    brakes_temperature: List[int]
    clutch: int
    drs: str
    engine_rpm: int
    engine_temperature: int
    gear: int
    rev_lights_bit_value: int
    rev_lights_percent: int
    speed: int
    steer: float
    surface_type: List[str]  # SURFACE_TYPES, 1 per corner of the car
    throttle: float
    tyres_inner_temperature: List[int]
    tyres_pressure: List[int]
    tyres_surface_temperature: List[int]


class TelemetryReadings(BaseModel):
    car_telemetry_data: List[CarTelemetryReading]
