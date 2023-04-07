from f1_22_telemetry.models.session import Session
from f1_22_telemetry.logic.session import build_session


def test_build_session(session_data):
    session: Session = build_session(session_data)
    assert len(session.dict().keys()) == 43
    assert len(session.weather_forecasts) == 6
    assert len(session.marshal_zones) == 17
