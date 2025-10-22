# Current MCU: STM32F103C8T6

from PySide6.QtCore import QObject, Signal, Slot

from mcu_communication_base import MCUCommunicationBase

class STM32Communication(MCUCommunicationBase):

    def __init__(self, parent=None) -> None:
        super().__init__(parent)

    def start_communication(self) -> None:
        print('Communication!')




def main() -> None:
    communication = STM32Communication()
    communication.start_communication()

if __name__ == '__main__':
    main()