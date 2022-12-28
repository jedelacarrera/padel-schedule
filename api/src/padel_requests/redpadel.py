from src.padel_requests.base import BaseClient
from src.memoization_decorator import cache_decorator


class RedPadelClient(BaseClient):
    URL = "https://www.tenissantuario.cl/booking/srvc.aspx/"

    HEADERS = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json; charset=UTF-8',
        # 'Cookie': 'ASP.NET_SessionId=jpyqdziuqj1tk3553mc2kiz0; cb-enabled=enabled; i18next=es-CL',
        'Origin': 'http://www.redpadel.cl',
        'Referer': 'http://www.redpadel.cl/Booking/Grid.aspx',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    COOKIES = {
        'ASP.NET_SessionId': 'jpyqdziuqj1tk3553mc2kiz0',
        'cb-enabled': 'enabled',
        'i18next': 'es-CL',
    }

    NAME = "RedPadel"
    FILTER = ""
    P = "eNEe29kXfZCYYTtFPL/1ufQZK/cQ2h54jPvOgWstpV0="

    @cache_decorator("redpadel", 120, index=1)
    def get_schedule(self, date: str):
        result = super().get_schedule(date)
        return result
