from abc import ABC, abstractmethod

from nebx.types import HTTPResponse


class IRequestWrapper(ABC):
    @abstractmethod
    async def get(self, url: str, headers: dict | None = None) -> HTTPResponse:
        pass

    @abstractmethod
    async def post(self, url: str, data: any, headers: dict | None = None) -> HTTPResponse:
        pass

    @abstractmethod
    async def close(self) -> None:
        pass
