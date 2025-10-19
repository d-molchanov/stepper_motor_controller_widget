import sys
from serial import Serial
from serial.tools.list_ports import comports
from serial.serialutil import SerialException
from PySide6.QtCore import QThread, Signal, QObject, Slot, QTimer, QCoreApplication, QDateTime
import time
import enum

class MCURequests(enum.Enum):
    # CHECKSTATE = '!QP%'.encode('utf-8')
    # SETZERO = '!ZE%'.encode('utf-8')
    # STOP = '!ST%'.encode('utf-8')
    CHECKSTATE = b'!QP%'
    SETZERO = b'!ZE%'
    STOP = b'!ST%'

class Status(enum.Enum):
    INFO = 'INFO'
    ERROR = 'ERROR'


class MCUCommunication(QObject):
    data_received = Signal(bytes)
    error_occured = Signal(bytes)
    finished = Signal()
    message_sent = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        self.port_name = None
        self.baudrate = None
        self.serial_port = None
        self.timer = None
        self.i = 0

    def format_message(self, msg: str, level: str) -> str:
        timestamp = QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss.zzz')
        return f'{timestamp} {level}: {msg}'

    def logs_update(self, msg: str, level: str) -> None:
        log_message = self.format_message(msg, level)
        self.message_sent.emit(log_message)

    @Slot(str)
    def set_port_name(self, port_name: str) -> None:
        self.port_name = port_name
        self.logs_update(
            f'Port `{self.port_name}` was chosen.',
            Status.INFO.value
        )

    @Slot(int)
    def set_baudrate(self, baudrate: int) -> None:
        self.baudrate = baudrate
        self.logs_update(
            f'Baudrate `{self.baudrate}` was chosen.',
            Status.INFO.value
        )

    @Slot(dict)
    def create_request(self, data: dict) -> bytes:
        print(data)

    @Slot()
    def start_communication(self) -> None:
        try:
            self.serial_port = Serial(self.port_name, self.baudrate, timeout=1)
        except SerialException as e:
            self.error_occured.emit(f'Port `{self.port_name}` could not be opened: {e}')
            print(f'Port `{self.port_name}` could not be opened: {e}')
            self.finished.emit()
            return 

        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.read_data)
        self.timer.start()

    # @Slot()
    def read_data(self) -> bytes | None:
        # print(f'{self.i = }')
        self.i += 1
        if not self.serial_port:
            return
        if not self.serial_port.is_open:
            return
        try:
            if self.serial_port.in_waiting > 0:
                data = self.serial_port.readline()
                # data = self.serial_port.read()
                # self.data_received.emit(data)
                print(data.decode('utf-8'))
        except SerialException as e:
            self.error_occured.emit(f'Reading error at `{self.port_name}`: {e}')

    @Slot(bytes)
    def write_data(self, data: bytes) -> None:
        if not self.serial_port:
            return
        if not self.serial_port.is_open:
            return 
        try:
            self.serial_port.write(data)
        except SerialException as e:
            self.error_occured.emit(f'Writing error at `{self.port_name}`: {e}')

    @Slot()
    def close_connection(self) -> None:
        if self.timer:
            self.timer.stop()
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
            self.finished.emit()

    @Slot()
    def check_state(self) -> None:
        # print(MCURequests.CHECKSTATE == '!QP%'.encode('utf-8'))
        self.write_data(MCURequests.CHECKSTATE.value)


    @Slot()
    def stop_motor(self) -> None:
        self.write_data(MCURequests.STOP.value)

    @Slot()
    def set_zero(self) -> None:
        self.write_data(MCURequests.SETZERO.value)

    # @Slot()
    # def check_port(self):
    #     if self.serial_port.in_waiting > 0:
    #         data = self.serial_port.readline()
    #         print(f'Message received: `{data.decode("utf-8")}')
    #         self.timer.stop()

    # def check_available_ports(self) -> list:
    #     return [port.device for port in comports()]

    # def connect_to_port(self, port, baud_rate) -> Serial:
    #     try:
    #         print(f'Initializing port `{port}` ...')
    #         serial_port = Serial(port, baud_rate, timeout=0.5)
    #         serial_port.flushInput()
    #         serial_port.flushOutput()
    #         self.active_port = port
    #         self.serial_port = serial_port
    #         print(f'Connection to port `{port}` has been established')
    #         return serial_port
    #     except SerialException as e:
    #         print(f'Port `{port}` could not be opened. Check connection')

    # def close_connection(self) -> None:
    #     if self.active_port:
    #         try:
    #             self.serial_port.close()
    #             print(f'Port `{self.active_port}` has been closed')
    #             self.active_port = None
    #             self.serial_port = None
    #         except SerialException as e:
    #             print(f'Port `{self.active_port}` could not be closed. Check connection')

    # @Slot()
    # def listen_port(self) -> None:
    #     while self.listen:
    #         if self.serial_port.in_waiting > 0:
    #             data = self.serial_port.readline()
    #             print(f'Message received: `{data.decode("utf-8")}')

    # def check_state(self)  -> None:
    #     if self.active_port:
    #         try:
    #             self.serial_port.write('!QP%'.encode('utf-8'))
    #             print('Message was sent')
    #             # time.sleep(2)
    #             print(self.serial_port.in_waiting)
    #             self.timer.start(1000)
                
    #             # while True:
    #             #     if self.serial_port.in_waiting > 0:
    #             #         data = self.serial_port.readline()
    #             #         # data = self.serial_port.read()
    #             #         print(f'Message received: `{data.decode("utf-8")}`')
    #             #         break
    #         except SerialException as e:
    #             print(f'Something wrong with {self.active_port}')

def main():
    print('This is main method!')
    app = QCoreApplication(sys.argv)
    communication = MCUCommunication('COM9')
    communication_thread = QThread()
    communication.moveToThread(communication_thread)
    communication_thread.started.connect(communication.start_communication)
    communication_thread.start()

    communication.finished.connect(communication_thread.quit)
    communication.finished.connect(communication.deleteLater)
    communication_thread.finished.connect(communication_thread.deleteLater)

    time.sleep(2)
    print('Wake up!')
    communication.write_data('!QP%'.encode('utf-8'))
    # communication.write_data(bytes([33,77,15,48,48,48,48,49,48,14,15,0,134,8,64,37]))
    communication.write_data(bytes([33,77,47,48,48,49,48,49,48,3,131,0,134,10,84,37]))
    communication.write_data('!QP%'.encode('utf-8'))
    time.sleep(5)
    communication.finished.emit()
    print('Finished!')
    sys.exit(app.exec())
    # communication = MCUCommunication()
    # ports = communication.check_available_ports()
    # print(f'{ports = }')
    # communication.connect_to_port('COM9', 9600)
    # communication.check_state()
    # communication.close_connection()

if __name__ == '__main__':
    main()