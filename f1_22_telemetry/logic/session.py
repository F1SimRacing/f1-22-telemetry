from typing import Dict, List

from f1_22_telemetry.appendices import BRAKING_ASSIST, DRS_ASSIST, DYNAMIC_RACING_LINE, DYNAMIC_RACING_LINE_TYPE
from f1_22_telemetry.appendices import ERS_ASSIST, FORECAST_ACCURACY, FORMULA, GAME_MODE_IDS, GEARBOX_ASSIST
from f1_22_telemetry.appendices import PIT_ASSIST, PIT_RELEASE_ASSIST, RULESET_IDS, SAFETY_CAR_STATUS, SESSION_LENGTH
from f1_22_telemetry.appendices import SLI_PRO_SUPPORT, STEERING_ASSIST, TRACK_IDS, WEATHER
from f1_22_telemetry.models.session import MarshalZone, Session, SessionType, WeatherForcastSample, WeatherForecast


def process_marshal_zones(zones: Dict):
    list_of_zones = []
    for zone in zones:
        if zone["zone_start"] == 0.0:
            continue
        list_of_zones.append(MarshalZone(**zone))

    return list_of_zones


def process_forecast_samples(weather_forecast_samples: Dict) -> Dict:
    forecasts = {}

    for forecast in weather_forecast_samples:
        cast = WeatherForcastSample(**forecast)
        session_type = SessionType(cast.session_type).name

        if session_type == SessionType(0).name:
            continue

        if session_type not in forecasts.keys():
            forecasts[session_type] = WeatherForecast(session_type=cast.session_type)

        if cast.time_offset == 0:
            forecasts[session_type].time_offset_0 = cast
        elif cast.time_offset == 5:
            forecasts[session_type].time_offset_5 = cast
        elif cast.time_offset == 10:
            forecasts[session_type].time_offset_10 = cast
        elif cast.time_offset == 15:
            forecasts[session_type].time_offset_15 = cast
        elif cast.time_offset == 30:
            forecasts[session_type].time_offset_30 = cast
        elif cast.time_offset == 45:
            forecasts[session_type].time_offset_45 = cast
        elif cast.time_offset == 60:
            forecasts[session_type].time_offset_60 = cast

    return forecasts


def build_session(packet: Dict) -> Session:
    return Session(
        ai_difficulty=packet['ai_difficulty'],
        air_temperature=packet['air_temperature'],
        braking_assist=BRAKING_ASSIST[packet['braking_assist']],
        drs_assist=DRS_ASSIST[packet['drs_assist']],
        dynamic_racing_line=DYNAMIC_RACING_LINE[packet['dynamic_racing_line']],
        dynamic_racing_line_type=DYNAMIC_RACING_LINE_TYPE[packet['dynamic_racing_line_type']],
        ers_assist=ERS_ASSIST[packet['ers_assist']],
        forecast_accuracy=FORECAST_ACCURACY[packet['forecast_accuracy']],
        formula=FORMULA[packet['formula']],
        game_mode=GAME_MODE_IDS[packet['game_mode']],
        game_paused=packet['pit_speed_limit'],
        gearbox_assist=GEARBOX_ASSIST[packet['gearbox_assist']],
        is_spectating=packet['is_spectating'],
        marshal_zones=process_marshal_zones(packet['marshal_zones']),
        network_game=packet['network_game'],
        num_marshal_zones=packet['num_marshal_zones'],
        num_weather_forecast_samples=packet['num_weather_forecast_samples'],
        pit_assist=PIT_ASSIST[packet['pit_assist']],
        pit_release_assist=PIT_RELEASE_ASSIST[packet['pit_release_assist']],
        pit_speed_limit=packet['pit_speed_limit'],
        pit_stop_rejoin_position=packet['pit_stop_rejoin_position'],
        pit_stop_window_ideal_lap=packet['pit_stop_window_ideal_lap'],
        pit_stop_window_latest_lap=packet['pit_stop_window_latest_lap'],
        rule_set=RULESET_IDS[packet['rule_set']],
        safety_car_status=SAFETY_CAR_STATUS[packet['safety_car_status']],
        season_link_identifier=packet['season_link_identifier'],
        session_duration=packet['session_duration'],
        session_length=SESSION_LENGTH[packet['session_length']],
        session_link_identifier=packet['session_link_identifier'],
        session_time_left=packet['session_time_left'],
        session_type=packet['session_type'],
        sli_pro_native_support=SLI_PRO_SUPPORT[packet['sli_pro_native_support']],
        spectator_car_index=packet['spectator_car_index'],
        steering_assist=STEERING_ASSIST[packet['steering_assist']],
        time_of_day=packet['time_of_day'],
        total_laps=packet['total_laps'],
        track_id=TRACK_IDS[packet['track_id']],
        track_length=packet['track_length'],
        track_temperature=packet['track_temperature'],
        weather=WEATHER[packet['weather']],
        weather_forecast_samples=packet['weather_forecast_samples'],
        weather_forecasts=process_forecast_samples(packet['weather_forecast_samples']),
        weekend_link_identifier=packet['weekend_link_identifier'],
    )
