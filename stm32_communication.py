# Current MCU: STM32F103C8T6
from enum import StrEnum
from serial import Serial
from serial.serialutil import SerialException
from serial.tools.list_ports import comports

from PySide6.QtCore import QObject, Signal, Slot, QTimer

from mcu_communication_base import MCUCommunicationBase

class Level(StrEnum):
    INFO = 'INFO'
    ERROR = 'ERROR'

class StmRequest(StrEnum):
    CHECKSTATE = '!QP%'
    SETZERO = '!ZE%'
    STOP = '!ST%'

class STM32Communication(MCUCommunicationBase):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.serial_port = None
        self.port_name = None
        self.baudrate = None
        self.timer = None
    
    @Slot(str, int)
    def start_communication(
        self,
        port_name: str,
        baudrate: int
    ) -> None:        
        try:
            self.port_name = port_name
            self.baudrate = baudrate
            self.update_logs(
                (
                    f'Trying to connect to `{self.port_name}` '
                    f'with baudrate {self.baudrate}'
                ),
                Level.INFO
            )
            self.serial_port = Serial(
                self.port_name,
                self.baudrate,
                timeout=1
            )
            self.update_logs(
                (
                    f'Connection to `{self.port_name}` '
                    f'with baudrate {self.baudrate} '
                    'has been established'
                ),
                Level.INFO
            )
            self.connection_is_active.emit(True)
        except SerialException as e:
            self.update_logs(
                f'Port `{self.port_name} could not be opened: {e}`',
                Level.ERROR
            )
            return
        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.read_data)
        self.timer.start()

    @Slot()
    def close_connection(self) -> None:
        if self.timer:
            self.timer.stop()
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
            self.connection_is_active.emit(False)
            self.update_logs(
                (
                    f'Connection to port `{self.port_name}` '
                    'has been closed'
                ),
                Level.INFO
            )

    def read_data(self) -> bytes | None:
        if not self.serial_port:
            return
        if not self.serial_port.is_open:
            return
        try:
            if self.serial_port.in_waiting <= 0:
                return 
            data = self.serial_port.readline()
            try:
                answer = data.decode('utf-8')
            except UnicodeError as e:
                self.update_logs(
                    f'Answer could not be decoded: {e}',
                    Level.ERROR
                )
                return
            self.update_logs(
                f'Answer has been received: `{answer}`',
                Level.INFO
            )
        except SerialException as e:
            self.update_logs(
                f'Reading error at `{self.port_name}`: {e}',
                Level.ERROR
            )

    @Slot(bytes)
    def write_data(self, data: bytes) -> None:
        if not self.serial_port:
            return
        if not self.serial_port.is_open:
            return 
        try:
            self.serial_port.write(data)
        except SerialException as e:
            self.update_logs(
                f'Writing error at `{self.port_name}`: {e}',
                Level.ERROR
            )
    
    @Slot()
    def check_state(self) -> None:
        self.update_logs(
            f'Request to STM32: `{StmRequest.CHECKSTATE}`', Level.INFO
        )
        self.write_data(StmRequest.CHECKSTATE.encode('utf-8'))
    
    @Slot()
    def stop_motor(self) -> None:
        self.update_logs(
            f'Request to STM32: `{StmRequest.STOP}`', Level.INFO
        )        
        self.write_data(StmRequest.STOP.encode('utf-8'))
    
    @Slot()
    def set_zero(self) -> None:
        self.update_logs(
            f'Request to STM32: `{StmRequest.SETZERO}`', Level.INFO
        )
        self.write_data(StmRequest.SETZERO.encode('utf-8'))

def main() -> None:
    communication = STM32Communication('COM9', 9600)
    communication.start_communication()
    communication.check_state()
    print('Done!')

if __name__ == '__main__':
    main()