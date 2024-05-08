# nebx (nebulaspace)

nebx is a python "Swiss Army knife" to orchestrate existing python packages, reducing boilerplate codes.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install nebx.

```bash
pip install nebx
```

## Quick Usage Overview

* Http request and Concurrency:

```python
import asyncio
from time import perf_counter

from nebx import RequestWrapperHttpx, HttpHeaderFaker, ConcurrentTaskManager
from nebx.interfaces import IRequestWrapper, IHttpHeaderFaker, IConcurrentTaskManager


async def main():
    task_manager: IConcurrentTaskManager = ConcurrentTaskManager()
    header_faker: IHttpHeaderFaker = HttpHeaderFaker()
    request: IRequestWrapper = RequestWrapperHttpx()

    for i in range(1, 100):
        header_faker.change_user_agent()
        coro = request.get(f"https://dummyjson.com/products/{i}", headers=header_faker.header)
        task = asyncio.create_task(coro)
        task_manager.add_task(task)

    start = perf_counter()
    responses = await task_manager.run_tasks()
    stop = perf_counter()
    print(stop - start, responses)
    await request.close()


if __name__ == '__main__':
    asyncio.run(main())
```

* Email :

```python
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from nebx import SmtpMailer
from nebx.types import MailerSetting
from nebx.interfaces import IMailer

# currently only support port 465 with ssl and basic text email
mail_setting = MailerSetting(
    smtp_server="any.smtp.domain.tld",
    username="your_address@domain.tld",
    password="your_strong_password",
    port=465
)
mailer: IMailer = SmtpMailer(mail_setting)

# soon update to build email content easier, stay tuned !
msg = MIMEMultipart()
msg["From"] = "your_address@domain.tld"
msg["To"] = "any_address@domain.tld"
msg["Subject"] = "Limited Time: 🚀 Unlock 40% Off All [nebx] Memberships!"
text = "Join [nebx]’s 200+ courses in FP&A, financial modeling, valuation, capital markets and more....."
msg.attach(MIMEText(text))

mailer.send(msg)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://github.com/enricoroselino/nebx/blob/main/license.txt)