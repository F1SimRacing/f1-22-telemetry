"""
Basic listener to read the UDP packet and convert it to a known packet format.
"""

import socket
from enum import Enum
from typing import Dict
from typing import Optional

from f1_22_telemetry.logic.car import build_car_telemetry
from f1_22_telemetry.logic.participants import build_participants
from f1_22_telemetry.models.session import Session
from f1_22_telemetry.logic.session import build_session
# from f1_22_telemetry.packets import PacketCarDamageData
# from f1_22_telemetry.packets import PacketCarSetupData
# from f1_22_telemetry.packets import PacketCarStatusData
# from f1_22_telemetry.packets import PacketCarTelemetryData
# from f1_22_telemetry.packets import PacketEventData
# from f1_22_telemetry.packets import PacketFinalClassificationData
from f1_22_telemetry.packets import PacketHeader, HEADER_FIELD_TO_PACKET_TYPE
# from f1_22_telemetry.packets import PacketLapData
# from f1_22_telemetry.packets import PacketLobbyInfoData
# from f1_22_telemetry.packets import PacketMotionData
# from f1_22_telemetry.packets import PacketParticipantsData
# from f1_22_telemetry.packets import PacketSessionData
# from f1_22_telemetry.packets import PacketSessionHistoryData


class PacketType(Enum):
    motion = (2022, 1, 0)
    session = (2022, 1, 1)
    lap = (2022, 1, 2)
    event = (2022, 1, 3)
    participants = (2022, 1, 4)
    car_setup = (2022, 1, 5)
    car_telemetry = (2022, 1, 6)
    car_status = (2022, 1, 7)
    final_classification = (2022, 1, 8)
    lobby_info = (2022, 1, 9)
    car_damage = (2022, 1, 10)
    session_history = (2022, 1, 11)


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
        elif key == PacketType.session:
            return build_session()
        elif key == (2022, 1, 2):
            pass
        elif key == (2022, 1, 3):
            pass
        elif key == (2022, 1, 4):
            return build_participants(packet)
        elif key == (2022, 1, 5):
            pass
        elif key == (2022, 1, 6):
            return build_car_telemetry(packet)
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

    def get_session(self) -> Session:
        return self.get_specific_packet(PacketType.session)

    def get_specific_packet(self, key: PacketType):
        found = False
        packet: Dict = {}

        for i in range(100):
            packet = self.get()
            header = packet['header']
            packet_key = (header.packet_format, header.packet_version, header.packet_id)

            if packet_key == key.value:
                break

        # build the packet and return it
        if key.value == (2022, 1, 0):
            pass
        elif key.value == (2022, 1, 1):
            return build_session(packet)
        elif key.value == (2022, 1, 2):
            pass
        elif key.value == (2022, 1, 3):
            pass
        elif key.value == (2022, 1, 4):
            return build_participants(packet)
        elif key.value == (2022, 1, 5):
            pass
        elif key.value == (2022, 1, 6):
            return build_car_telemetry(packet)
        elif key.value == (2022, 1, 7):
            pass
        elif key.value == (2022, 1, 8):
            pass
        elif key.value == (2022, 1, 9):
            pass
        elif key.value == (2022, 1, 10):
            pass
        elif key.value == (2022, 1, 11):
            pass
        else:
            pass
