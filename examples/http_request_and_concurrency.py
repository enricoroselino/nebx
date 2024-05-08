import asyncio
from time import perf_counter

from nebx import RequestWrapperHttpx, HttpHeaderFaker, ConcurrentTaskManager
from nebx.interfaces import IRequestWrapper, IHttpHeaderFaker, IConcurrentTaskManager


async def main():
    task_manager: IConcurrentTaskManager = ConcurrentTaskManager()
    header_faker: IHttpHeaderFaker = HttpHeaderFaker()
    request: IRequestWrapper = RequestWrapperHttpx()

    start = perf_counter()
    for i in range(1, 100):
        header_faker.change_user_agent()
        coro = request.get(f"https://dummyjson.com/products/{i}", headers=header_faker.header)
        task = asyncio.create_task(coro)
        task_manager.add_task(task)

    responses = await task_manager.run_tasks()
    stop = perf_counter()
    print(stop - start, responses)
    await request.close()


if __name__ == '__main__':
    asyncio.run(main())
