import asyncio
import httpx

from nebx.interfaces import IRequestWrapper
from nebx.types import HTTPResponse


class RequestWrapperHttpx(IRequestWrapper):
    def __init__(self, proxy: str | None = None, ssl_strict: bool = True):
        self.__ssl_strict = ssl_strict
        self.__proxy = proxy
        self.__client_session = self.__create_client()

    async def get(self, url: str, headers: dict | None = None) -> HTTPResponse:
        try:
            response = await self.__client_session.get(url, headers=headers)
            return_response = await _httpx_response_handler(response)
        except Exception as ex:
            return_response = HTTPResponse(text=str(ex), status_code=999)
        return return_response

    async def post(self, url: str, data: any, headers: dict | None = None):
        try:
            response = await self.__client_session.post(url, data=data, headers=headers)
            return_response = await _httpx_response_handler(response)
        except Exception as ex:
            return_response = HTTPResponse(text=str(ex), status_code=999)
        return return_response

    async def close(self) -> None:
        await self.__client_session.aclose()
        await asyncio.sleep(0.250)

    def __create_client(self) -> httpx.AsyncClient:
        return httpx.AsyncClient(proxy=self.__proxy, verify=self.__ssl_strict)


async def _httpx_response_handler(response: httpx.Response) -> HTTPResponse:
    status_code: int = 999
    return_response: HTTPResponse

    try:
        status_code = response.status_code
        response.raise_for_status()
        return_response = HTTPResponse(text=response.text, status_code=status_code)
        await response.aclose()
    except httpx.HTTPStatusError as status_error:
        return_response = HTTPResponse(text=str(status_error), status_code=status_code)
    except Exception as ex:
        return_response = HTTPResponse(text=str(ex), status_code=status_code)

    return return_response
