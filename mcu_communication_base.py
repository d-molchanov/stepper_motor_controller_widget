from PySide6.QtCore import QObject, Signal, QDateTime


class MCUCommunicationBase(QObject): 
    connection_is_active = Signal(bool)
    logs_updated = Signal(str)

    def __init__(self, parent = None) -> None:
        super().__init__(parent)


    def _format_log_message(self, msg: str, level: str) -> str:
        timestamp = QDateTime.currentDateTime().toString(
            'yyyy-MM-dd HH:mm:ss.zzz'
        )
        return f'{timestamp} {level}: {msg}'
    
    def update_logs(self, msg: str, level: str) -> None:
        log_message = self._format_log_message(msg, level)
        self.logs_updated.emit(log_message)

    def start_communication(self) -> None:
        raise NotImplementedError()
    
    def stop_communication(self) -> None:
        raise NotImplementedError()
    
    def read_data(self) -> bytes:
        raise NotImplementedError()
    
    def write_data(self, data: bytes) -> None:
        raise NotImplementedError()
    

def main() -> None:
    communication = MCUCommunicationBase()
    communication.start_communication()

if __name__ == '__main__':
    main()