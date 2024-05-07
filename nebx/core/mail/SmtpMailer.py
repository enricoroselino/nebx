import smtplib
import ssl
from email.mime.multipart import MIMEMultipart

from nebx.types import MailerSetting
from nebx.interfaces.IMailer import IMailer


class SmtpMailer(IMailer):
    def __init__(self, mailer_setting: MailerSetting):
        self.__SSL_CONTEXT = ssl.create_default_context()
        self.__smtp_server = mailer_setting.smtp_server
        self.__username = mailer_setting.username
        self.__password = mailer_setting.password
        self.__port = 465

    @property
    def sender(self) -> str:
        return self.__username

    def send(self, message: MIMEMultipart, timeout: int = 30) -> bool:
        sent_status = False
        to = str(message["To"]).split(",")
        bcc = str(message["Bcc"]).split(",")
        cc = str(message["Cc"]).split(",")
        sender = message["From"] or self.__username

        try:
            with smtplib.SMTP_SSL(self.__smtp_server, self.__port, context=self.__SSL_CONTEXT,
                                  timeout=timeout) as server:
                server.login(self.__username, self.__password)
                server.send_message(message, sender, to + bcc + cc)
                sent_status = True
        except Exception as ex:
            print(ex)
        return sent_status
