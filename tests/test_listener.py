from unittest.mock import MagicMock

from f1_22_telemetry.listener import PacketType, TelemetryListener
from f1_22_telemetry.models.session import Session
from f1_22_telemetry.packets import PacketHeader


def test_listener_get_specific_packet_session(session_data):
    header = PacketHeader()

    header.packet_format = 2022
    header.packet_version = 1
    header.packet_id = 1

    session_data['header'] = header

    listener = TelemetryListener()
    mock_get = MagicMock()
    mock_get.return_value = lambda: session_data

    listener.get = mock_get()
    packet = listener.get_specific_packet(PacketType.session)
    assert instance(packet, Session)
