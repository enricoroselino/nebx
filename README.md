# nebx (nebulaspace)

nebx is a python "Swiss Army knife" to orchestrate existing python packages, reducing boilerplate codes.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install nebx.

```bash
pip install nebx
```

## Quick Usage Overview

```python
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
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://github.com/enricoroselino/nebx/blob/main/license.txt)