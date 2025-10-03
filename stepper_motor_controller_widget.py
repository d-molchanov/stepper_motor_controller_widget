from serial import Serial
from serial.tools.list_ports import comports

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from ui_stepper_motor_controller_widget import Ui_Form


class StepperMotorControllerWidget(QWidget, Ui_Form):
	def __init__(self) -> None:
		super().__init__()
		self.setupUi(self)
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
		self.pushButtonConnect.clicked.connect(self.test)

	def check_available_comports(self) -> list:
		return [
			port.device for port in comports()
		]

	@Slot()
	def test(self):
		print(f'{self.comboBoxCOMPorts.currentText()} - {self.comboBoxBaudRate.currentText()}')
