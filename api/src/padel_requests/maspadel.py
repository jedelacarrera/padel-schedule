from src.padel_requests.base import BaseClient
from src.memoization_decorator import cache_decorator


class MasPadelClient(BaseClient):
    URL = "http://www.maspadel.cl/booking/srvc.aspx/"

    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",  # pylint: disable=line-too-long
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/json; charset=utf-8",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "http://www.maspadel.cl",
        "Connection": "keep-alive",
        "Referer": "http://www.maspadel.cl/Booking/Grid.aspx",
    }

    COOKIES = {
        "ASP.NET_SessionId": "f5vqhj2shi4ioq3hxqdfignj",
        "cb-enabled": "accepted",
        "i18next": "es-ES",
    }

    NAME = "Más Padel"
    FILTER = "PÁDEL"
    DEFAULT_END_TIME = "23:00"

    @cache_decorator("maspadel", 120, index=1)
    def get_schedule(self, date: str):
        return super().get_schedule(date)
