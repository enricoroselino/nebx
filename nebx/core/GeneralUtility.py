from typing import Coroutine
import csv
from iteration_utilities import unique_everseen
from urllib.parse import urlparse
from typing import Iterable


async def async_task_sequence(coroutines: list[Coroutine]) -> None:
    for coro in coroutines:
        await coro


def read_csv(file_path: str, delimiter: str = ",", remove_duplicates: bool = False) -> list[dict]:
    data = []
    with open(file_path, "r") as file:
        reader = csv.DictReader(file, delimiter=delimiter)
        for row in reader:
            data.append(row)

    return data if remove_duplicates is False else remove_duplicate(data)


def remove_duplicate(data: Iterable) -> list[any]:
    return list(unique_everseen(data))


def get_domain_name(url: str) -> str:
    result = urlparse(url)
    return result.netloc
