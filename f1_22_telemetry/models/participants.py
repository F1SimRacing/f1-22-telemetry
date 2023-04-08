from typing import Dict, List

from pydantic import BaseModel


class Driver(BaseModel):
    ai_controlled: int
    my_team: int
    name: str
    nationality: str
    network_id: int
    race_number: int
    team_name: str
    your_telemetry: int


class Drivers(BaseModel):
    drivers: List[Driver]
