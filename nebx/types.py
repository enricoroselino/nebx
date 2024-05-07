from dataclasses import dataclass
from json import loads


@dataclass
class HTTPResponse:
    text: str
    status_code: int

    def json(self):
        return loads(self.text) if self.text is not None else {}


@dataclass
class MailerSetting:
    smtp_server: str
    username: str
    password: str
    port: int
