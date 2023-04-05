from typing import List

from pydantic import BaseModel


class LapHistory(BaseModel):
    lap_time_in_ms: int
    sector1_time_in_ms: int
    sector2_time_in_ms: int
    sector3_time_in_ms: int
    lap_valid_bit_flags: int


class TyreStintHistory(BaseModel):
    end_lap: int
    tyre_actual_compound: str
    tyre_visual_compound: str


class LapData(BaseModel):
    best_lap_time_lap_num: int
    best_sector1_lap_num: int
    best_sector2_lap_num: int
    best_sector3_lap_num: int
    num_laps: int
    num_tyre_stints: int
    lap_history_data: List[LapHistory]
    tyre_stints_history_data: List[TyreStintHistory]


class Lap(BaseModel):
    car_position: int
    current_lap_invalid: int
    current_lap_num: int
    current_lap_time_in_ms: int
    # Status of driver - 0 = in garage, 1 = flying lap
    # // 2 = in lap, 3 = out lap, 4 = on track
    driver_status: int
    grid_position: int
    lap_distance: float
    last_lap_time_in_ms: int
    num_pit_stops: int
    num_unserved_drive_through_pens: int
    num_unserved_stop_go_pens: int
    penalties: int
    pit_lane_time_in_lane_in_ms: int
    pit_lane_timer_active: int
    pit_status: int
    pit_stop_should_serve_pen: int
    pit_stop_timer_in_ms: int
    # status - 0 = invalid, 1 = inactive, 2 = active
    # 3 = finished, 4 = didnotfinish, 5 = disqualified
    result_status: int
    safety_car_delta: float
    sector: int
    sector1_time_in_ms: int
    sector2_time_in_ms: int
    total_distance: float
    warnings: int
