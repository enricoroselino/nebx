from typing import Coroutine


async def async_task_sequence(coroutines: list[Coroutine]) -> None:
    for coro in coroutines:
        await coro
