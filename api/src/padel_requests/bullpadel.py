from src.padel_requests.base import BaseClient
from src.memoization_decorator import cache_decorator


class BullPadelClient(BaseClient):
    URL = "http://www.bullpadelcenter.cl/booking/srvc.aspx/ObtenerCuadro"

    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",  # pylint: disable=line-too-long
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/json; charset=utf-8",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "http://www.bullpadelcenter.cl",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "http://www.bullpadelcenter.cl/Booking/Grid.aspx",
    }

    COOKIES = {
        "ASP.NET_SessionId": "q420jcysx4farw45bnibc4vz",
        "cb-enabled": "enabled",
        "i18next": "es-CL",
    }

    NAME = "Bull Padel"
    FILTER = "Cancha"

    @cache_decorator("bullpadel", 60, index=1)
    def get_schedule(self, date: str):
        result = super().get_schedule(date)
        return result
