from abc import ABC, abstractmethod


class IHttpHeaderFaker(ABC):
    @abstractmethod
    def change_user_agent(self, values: str = None) -> None:
        pass

    @property
    @abstractmethod
    def header(self):
        pass
