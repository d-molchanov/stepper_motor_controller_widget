from serial import Serial
from serial.tools.list_ports import comports
from serial.serialutil import SerialException
from PySide6.QtCore import QThread, Signal, QObject, Slot, QTimer
import time


class MCUCommunication(QObject):

    def __init__(self):
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_port)

    @Slot()
    def check_port(self):
        if self.serial_port.in_waiting > 0:
            data = self.serial_port.readline()
            print(f'Message received: `{data.decode("utf-8")}')
            self.timer.stop()

    def check_available_ports(self) -> list:
        return [port.device for port in comports()]

    def connect_to_port(self, port, baud_rate) -> Serial:
        try:
            print(f'Initializing port `{port}` ...')
            serial_port = Serial(port, baud_rate, timeout=0.5)
            serial_port.flushInput()
            serial_port.flushOutput()
            self.active_port = port
            self.serial_port = serial_port
            print(f'Connection to port `{port}` has been established')
            return serial_port
        except SerialException as e:
            print(f'Port `{port}` could not be opened. Check connection')

    def close_connection(self) -> None:
        if self.active_port:
            try:
                self.serial_port.close()
                print(f'Port `{self.active_port}` has been closed')
                self.active_port = None
                self.serial_port = None
            except SerialException as e:
                print(f'Port `{self.active_port}` could not be closed. Check connection')

    @Slot()
    def listen_port(self) -> None:
        while self.listen:
            if self.serial_port.in_waiting > 0:
                data = self.serial_port.readline()
                print(f'Message received: `{data.decode("utf-8")}')

    def check_state(self)  -> None:
        if self.active_port:
            try:
                self.serial_port.write('!QP%'.encode('utf-8'))
                print('Message was sent')
                # time.sleep(2)
                print(self.serial_port.in_waiting)
                self.timer.start(1000)
                
                # while True:
                #     if self.serial_port.in_waiting > 0:
                #         data = self.serial_port.readline()
                #         # data = self.serial_port.read()
                #         print(f'Message received: `{data.decode("utf-8")}`')
                #         break
            except SerialException as e:
                print(f'Something wrong with {self.active_port}')

def main():
    print('This is main method!')
    communication = MCUCommunication()
    ports = communication.check_available_ports()
    print(f'{ports = }')
    communication.connect_to_port('COM9', 9600)
    communication.check_state()
    communication.close_connection()

if __name__ == '__main__':
    main()