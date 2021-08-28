from src.padel_requests.base import BaseClient
from src.memoization_decorator import cache_decorator


class RedPadelClient(BaseClient):
    URL = "https://www.tenissantuario.cl/booking/srvc.aspx/"

    HEADERS = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",  # pylint: disable=line-too-long
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/json; charset=utf-8",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "http://www.redpadel.cl",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "http://www.redpadel.cl/Booking/Grid.aspx",
    }

    COOKIES = {
        "ASP.NET_SessionId": "mz3xamauli2j12zfgsndwj45",
        "cb-enabled": "enabled",
        "i18next": "es-CL",
    }

    NAME = "RedPadel"
    FILTER = ""

    @cache_decorator("redpadel", 120, index=1)
    def get_schedule(self, date: str):
        result = super().get_schedule(date)
        return result
