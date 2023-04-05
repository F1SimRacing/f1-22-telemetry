"""
Basic listener to read the UDP packet and convert it to a known packet format.
"""

import socket
from typing import Optional

from f1_22_telemetry.models.session import Session
from f1_22_telemetry.models.session import build_session
from f1_22_telemetry.packets import PacketCarDamageData
from f1_22_telemetry.packets import PacketCarSetupData
from f1_22_telemetry.packets import PacketCarStatusData
from f1_22_telemetry.packets import PacketCarTelemetryData
from f1_22_telemetry.packets import PacketEventData
from f1_22_telemetry.packets import PacketFinalClassificationData
from f1_22_telemetry.packets import PacketHeader, HEADER_FIELD_TO_PACKET_TYPE
from f1_22_telemetry.packets import PacketLapData
from f1_22_telemetry.packets import PacketLobbyInfoData
from f1_22_telemetry.packets import PacketMotionData
from f1_22_telemetry.packets import PacketParticipantsData
from f1_22_telemetry.packets import PacketSessionData
from f1_22_telemetry.packets import PacketSessionHistoryData


class TelemetryListener:
    def __init__(self, host: Optional[str] = None, port: Optional[int] = None):

        # Set to default port used by the game in telemetry setup.
        if not port:
            port = 20777

        if not host:
            host = 'localhost'

        self.socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.socket.bind((host, port))

    def get(self):
        packet = self.socket.recv(2048)
        header = PacketHeader.from_buffer_copy(packet)

        key = (header.packet_format, header.packet_version, header.packet_id)

        return HEADER_FIELD_TO_PACKET_TYPE[key].unpack(packet)

    def get_packet(self):
        packet = self.socket.recv(2048)
        header = PacketHeader.from_buffer_copy(packet)

        key = (header.packet_format, header.packet_version, header.packet_id)

        # (2022, 1, 0): PacketMotionData,
        # (2022, 1, 1): PacketSessionData,
        # (2022, 1, 2): PacketLapData,
        # (2022, 1, 3): PacketEventData,
        # (2022, 1, 4): PacketParticipantsData,
        # (2022, 1, 5): PacketCarSetupData,
        # (2022, 1, 6): PacketCarTelemetryData,
        # (2022, 1, 7): PacketCarStatusData,
        # (2022, 1, 8): PacketFinalClassificationData,
        # (2022, 1, 9): PacketLobbyInfoData,
        # (2022, 1, 10): PacketCarDamageData,
        # (2022, 1, 11): PacketSessionHistoryData,
        packet = HEADER_FIELD_TO_PACKET_TYPE[key].unpack(packet)
        if key == (2022, 1, 0):
            pass
        elif key == (2022, 1, 1):
            return build_session()
        elif key == (2022, 1, 2):
            pass
        elif key == (2022, 1, 3):
            pass
        elif key == (2022, 1, 4):
            pass
        elif key == (2022, 1, 5):
            pass
        elif key == (2022, 1, 6):
            pass
        elif key == (2022, 1, 7):
            pass
        elif key == (2022, 1, 8):
            pass
        elif key == (2022, 1, 9):
            pass
        elif key == (2022, 1, 10):
            pass
        elif key == (2022, 1, 11):
            pass
        else:
            pass