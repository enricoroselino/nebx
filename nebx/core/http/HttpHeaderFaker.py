from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem, Popularity, SoftwareType, HardwareType, \
    SoftwareEngine

from nebx.interfaces.IHttpHeaderFaker import IHttpHeaderFaker


class HttpHeaderFaker(IHttpHeaderFaker):
    def __init__(self, init_header: dict[str, str] | None = None):
        self.__headers = init_header or {}
        self.__user_agents: UserAgent = self.__user_agent_factory()
        self.change_user_agent()

    @property
    def header(self):
        return self.__headers

    def change_user_agent(self, values: str = None) -> None:
        self.__headers.update({"User-Agent": values or str(self.__user_agents.get_random_user_agent())})

    @staticmethod
    def __user_agent_factory() -> UserAgent:
        software_names = [SoftwareName.CHROME.value, SoftwareName.SAFARI.value, SoftwareName.OPERA.value,
                          SoftwareName.FIREFOX.value]
        operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.IOS.value, OperatingSystem.CHROMEOS.value]
        popularity = [Popularity.AVERAGE.value, Popularity.POPULAR.value]
        hardware_types = [HardwareType.COMPUTER.value, HardwareType.MOBILE__TABLET.value, HardwareType.MOBILE.value]
        software_engines = [SoftwareEngine.GECKO.value, SoftwareEngine.WEBKIT.value]
        software_types = [SoftwareType.WEB_BROWSER.value]

        generated_user_agents = UserAgent(software_names=software_names,
                                          operating_systems=operating_systems,
                                          popularity=popularity,
                                          software_types=software_types,
                                          hardware_types=hardware_types,
                                          software_engines=software_engines,
                                          limit=50)

        return generated_user_agents
