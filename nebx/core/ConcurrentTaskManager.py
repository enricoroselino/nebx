import asyncio
from typing import Self

from nebx.interfaces.IConcurrentTaskManager import IConcurrentTaskManager


class ConcurrentTaskManager(IConcurrentTaskManager):
    def __init__(self):
        self.__tasks = []

    def add_task(self, task: asyncio.Task) -> Self:
        self.__tasks.append(task)
        return self

    async def run_tasks(self) -> tuple[any]:
        result = await asyncio.gather(*self.__tasks)
        self.__tasks.clear()
        return result
