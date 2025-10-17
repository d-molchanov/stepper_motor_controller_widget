from datetime import datetime

from serial import Serial
from serial.tools.list_ports import comports

from PySide6.QtCore import Signal, Slot, QTime, QDateTime
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from ui_stepper_motor_controller_widget import Ui_Form


class StepperMotorControllerWidget(QWidget, Ui_Form):
    logs_updated = Signal(str)
    connection_established = Signal(bool)
    com_port_chosen = Signal(str)
    baudrate_chosen = Signal(int)
    connection_requested = Signal()
    disconnection_requested = Signal()
    request_created = Signal(dict)

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.serial_port = None
        self.port_name = None
        self.baudrate = 0
        comports = self.check_available_comports()
        self.comboBoxCOMPorts.addItems(comports)
        self.comboBoxBaudRate.addItems(
            [
                '9600',
                '19200',
                '38400',
                '57600',
                '115200'
            ]
        )
        self.pushButtonConnect.clicked.connect(self.connect_to_port)
        self.pushButtonDisconnect.clicked.connect(self.disconnect_from_port)
        self.logs_updated.connect(self.update_logs)
        self.connection_established.connect(self.unable_button)
        self.pushButtonRefresh.clicked.connect(self.update_ports_list)
        self.pushButtonClearLogs.clicked.connect(self.textEditLogs.clear)
        self.comboBoxDirection.addItems(
            [
                'Clockwise', 
                'Conterclockwise'
            ]
        )
        step_values = ['1:1', '1:2', '1:4', '1:8', '1:16']
        self.comboBoxStep.addItems(step_values)
        self.comboBoxStep.setCurrentIndex(len(step_values)-1)
        self.pushButtonStartMotor.clicked.connect(self.create_request)

    def create_request(self) -> dict:
        result = {
            'step': self.comboBoxStep.currentText()
        }
        self.request_created.emit(result)

    def check_available_comports(self) -> list:
        return [
            port.device for port in comports()
        ]

    @Slot()
    def update_ports_list(self):
        self.comboBoxCOMPorts.clear()
        comports = self.check_available_comports()
        self.comboBoxCOMPorts.addItems(comports)

    @Slot(str)
    def update_logs(self, msg: str) -> None:
        self.textEditLogs.append(msg)

    @Slot(bool)
    def unable_button(self, value: bool) -> None:
        self.pushButtonConnect.setEnabled(value)
        self.comboBoxCOMPorts.setEnabled(value)
        self.comboBoxBaudRate.setEnabled(value)
        self.pushButtonRefresh.setEnabled(value)
        self.pushButtonDisconnect.setEnabled(not value)
        self.pushButtonSend.setEnabled(not value)
        self.pushButtonStartMotor.setEnabled(not value)
        self.pushButtonStopMotor.setEnabled(not value)
        self.pushButtonSetZero.setEnabled(not value)
        self.pushButtonCheckState.setEnabled(not value)

    @Slot()
    def disconnect_from_port(self):
        self.connection_established.emit(True)
        self.disconnection_requested.emit()
        msg = f'Connection to {self.port_name} has been closed.' 
        self.logs_updated.emit(
            self.format_message(msg, 'INFO')
        )

    def format_message(self, msg: str, level: str) -> str:
        timestamp = QDateTime.currentDateTime().toString('yyyy-MM-dd HH:mm:ss.zzz')
        return f'{timestamp} {level}: {msg}'

    @Slot()
    def connect_to_port(self):
        self.port_name = self.comboBoxCOMPorts.currentText()
        self.com_port_chosen.emit(self.port_name)
        self.baudrate = self.comboBoxBaudRate.currentText()
        self.baudrate_chosen.emit(int(self.baudrate))
        self.connection_requested.emit()
        self.connection_established.emit(False)
        msg = f'Connection to {self.port_name} with baudrate {self.baudrate} has been established.' 
        self.logs_updated.emit(
            self.format_message(msg, 'INFO')
        )
        # self.logs_updated.emit(f'{self.port_name} - {self.baudrate}')
        # print(f'{self.comboBoxCOMPorts.currentText()} - {self.comboBoxBaudRate.currentText()}')
