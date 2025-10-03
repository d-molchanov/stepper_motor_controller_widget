import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QStyleFactory
from stepper_motor_controller_widget import StepperMotorControllerWidget


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create('Fusion'))
    main_window = QMainWindow()
    main_window.resize(500, 300)
    main_widget = StepperMotorControllerWidget()
    main_window.setCentralWidget(main_widget)
    main_window.show()
    sys.exit(app.exec())