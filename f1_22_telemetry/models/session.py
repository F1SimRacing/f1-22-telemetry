from enum import Enum
from typing import Dict, List

from pydantic import BaseModel


class MarshalZone(BaseModel):
    # -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
    zone_flag: str
    # percentage around the track from 0 to 1
    zone_start: float


class WeatherForcastSample(BaseModel):
    air_temperature: int  # in Celsius
    air_temperature_change: int  # 0 up, 1 down and 2 no change
    rain_percentage: int  # Rain percentage (0-100)
    session_type: int
    time_offset: int  # Time in minutes the forecast is for
    track_temperature: int  # in Celsius
    track_temperature_change: int  # 0 up, 1 down and 2 no change
    # Weather - 0 = clear, 1 = light cloud, 2 = overcast
    # 3 = light rain, 4 = heavy rain, 5 = storm
    weather: int


class WeatherForecast(BaseModel):
    session_type: int
    time_offset_0: WeatherForcastSample | None
    time_offset_5: WeatherForcastSample | None
    time_offset_10: WeatherForcastSample | None
    time_offset_15: WeatherForcastSample | None
    time_offset_30: WeatherForcastSample | None
    time_offset_45: WeatherForcastSample | None
    time_offset_60: WeatherForcastSample | None


class Session(BaseModel):
    marshal_zones: List[MarshalZone]
    # Weather - 0 = clear, 1 = light cloud, 2 = overcast
    # 3 = light rain, 4 = heavy rain, 5 = storm
    weather: str
    track_temperature: int  # Track temp. in degrees celsius
    air_temperature: int  # Air temp. in degrees celsius
    total_laps: int  # Total number of laps in this race
    track_length: float  # Track length in metres
    # 0 = unknown, 1 = P1, 2 = P2, 3 = P3, 4 = Short P, 5 = Q1
    # 6 = Q2, 7 = Q3, 8 = Short Q, 9 = OSQ, 10 = R, 11 = R2
    # 12 = R3, 13 = Time Trial
    session_type: str
    track_id: str  # -1 for unknown, see appendix
    # Formula, 0 = F1 Modern, 1 = F1 Classic, 2 = F2,
    # 3 = F1 Generic, 4 = Beta, 5 = Supercars
    # 6 = ESports, 7 = F2 2021
    formula: str
    session_time_left: int  # Time left in session in seconds
    session_duration: int  # Session duration in seconds
    pit_speed_limit: int  # Pit speed limit in kilometres per hour
    game_paused: int  # Whether the game is paused
    is_spectating: int  # Whether the player is spectating
    spectator_car_index: int  # Index of the car being spectated
    # SLI Pro support, 0 = inactive, 1 = active
    sli_pro_native_support: str
    num_marshal_zones: int  # Number of marshal zones to follow
    # 0 = no safety car, 1 = full, 2 = virtual, 3 = formation lap
    safety_car_status: str
    network_game: int  # 0 = offline, 1 = online
    num_weather_forecast_samples: int
    # Number of weather samples to follow
    weather_forecast_samples: List[Dict]
    # Array of weather forecast samples
    forecast_accuracy: str  # 0 = Perfect, 1 = Approximate
    ai_difficulty: int  # AI Difficulty rating – 0-110
    season_link_identifier: int
    # Identifier for season - persists across saves
    weekend_link_identifier: int
    # Identifier for weekend - persists across saves
    session_link_identifier: int
    # Identifier for session - persists across saves
    pit_stop_window_ideal_lap: int
    # Ideal lap to pit on for current strategy (player)
    pit_stop_window_latest_lap: int
    # Latest lap to pit on for current strategy (player)
    pit_stop_rejoin_position: int  # Predicted position to rejoin at (player)
    steering_assist: str  # 0 = off, 1 = on
    braking_assist: str  # 0 = off, 1 = low, 2 = medium, 3 = high
    gearbox_assist: str  # 1 = manual, 2 = manual & suggested gear, 3 = auto
    pit_assist: str  # 0 = off, 1 = on
    pit_release_assist: str  # 0 = off, 1 = on
    ers_assist: str  # 0 = off, 1 = on
    drs_assist: str  # 0 = off, 1 = on
    dynamic_racing_line: str  # 0 = off, 1 = corners only, 2 = full
    dynamic_racing_line_type: str  # 0 = 2D, 1 = 3D
    game_mode: str  # Game mode id - see appendix
    rule_set: str  # Ruleset - see appendix
    time_of_day: int  # Local time of day - minutes since midnight
    # 0 = None, 2 = Very Short, 3 = Short, 4 = Medium
    # 5 = Medium Long, 6 = Long, 7 = Full
    session_length: str
    weather_forecasts: Dict


class SessionType(Enum):
    unknown = 0
    practice_1 = 1
    practice_2 = 2
    practice_3 = 3
    short_practice = 4
    qualifying_1 = 5
    qualifying_2 = 6
    qualifying_3 = 7
    short_qualifying = 8
    one_shot_qualifying = 9
    race = 10
    race_2 = 11
    race_3 = 12
    time_trial = 13
