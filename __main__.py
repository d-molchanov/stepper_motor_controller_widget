import sys
from PySide6.QtCore import QThread
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStyleFactory
from stepper_motor_controller_widget import StepperMotorControllerWidget
from port_listener import PortListener
from port_listener import MCUCommunication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    main_window = QMainWindow()
    main_window.resize(620, 300)
    main_widget = StepperMotorControllerWidget()
    main_window.setCentralWidget(main_widget)

    port_listener = PortListener()
    listener_thread = QThread()
    port_listener.moveToThread(listener_thread)

    communication = MCUCommunication()
    communication_thread = QThread()
    communication.moveToThread(communication_thread)

    main_window.show()
    sys.exit(app.exec())