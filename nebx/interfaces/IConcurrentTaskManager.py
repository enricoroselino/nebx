from abc import ABC, abstractmethod
import asyncio
from typing import Self


class IConcurrentTaskManager(ABC):
    @abstractmethod
    def add_task(self, task: asyncio.Task) -> Self:
        pass

    @abstractmethod
    async def run_tasks(self) -> tuple[any]:
        pass
