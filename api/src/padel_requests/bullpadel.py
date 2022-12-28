from src.padel_requests.base import BaseClient
from src.memoization_decorator import cache_decorator


class BullPadelClient(BaseClient):
    URL = "http://www.bullpadelcenter.cl/booking/srvc.aspx/"

    HEADERS = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json; charset=UTF-8",
        # 'Cookie': 'ASP.NET_SessionId=ta5eny55hhaftr45m0tgfomt; cb-enabled=enabled; i18next=es-CL',
        "Origin": "http://www.bullpadelcenter.cl",
        "Referer": "http://www.bullpadelcenter.cl/Booking/Grid.aspx",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",  # pylint: disable=line-too-long
        "X-Requested-With": "XMLHttpRequest",
    }

    COOKIES = {
        "ASP.NET_SessionId": "ta5eny55hhaftr45m0tgfomt",
        "cb-enabled": "enabled",
        "i18next": "es-CL",
    }

    NAME = "Bull Padel"
    P = "eNEe29kXfZCYYTtFPL/1ufji6catFXxwb/Soqc/74hI="

    @cache_decorator("bullpadel", 120, index=1)
    def get_schedule(self, date: str):
        result = super().get_schedule(date)
        return result
