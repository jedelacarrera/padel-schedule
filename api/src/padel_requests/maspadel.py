from src.padel_requests.base import BaseClient
from src.memoization_decorator import cache_decorator


class MasPadelClient(BaseClient):
    URL = "http://www.maspadel.cl/booking/srvc.aspx/"

    HEADERS = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json; charset=UTF-8',
        # 'Cookie': 'ASP.NET_SessionId=xchxyc5515e20j45rd04gz55; i18next=es-CL',
        'Origin': 'http://www.maspadel.cl',
        'Referer': 'http://www.maspadel.cl/Booking/Grid.aspx',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    COOKIES = {
        'ASP.NET_SessionId': 'xchxyc5515e20j45rd04gz55',
        'i18next': 'es-CL',
    }

    NAME = "Más Padel"
    FILTER = "PÁDEL"
    DEFAULT_END_TIME = "23:00"
    P = "eNEe29kXfZCYYTtFPL/1ufQZK/cQ2h54lsN2A7wYnIY="

    @cache_decorator("maspadel", 120, index=1)
    def get_schedule(self, date: str):
        return super().get_schedule(date)
