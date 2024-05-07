from abc import ABC, abstractmethod
from email.mime.multipart import MIMEMultipart


class IMailer(ABC):
    @property
    @abstractmethod
    def sender(self) -> str:
        pass

    @abstractmethod
    def send(self, message: MIMEMultipart, timeout: int = 30) -> bool:
        pass
