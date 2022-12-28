from src.padel_requests.base import BaseClient
from src.memoization_decorator import cache_decorator


class AltoPadelClient(BaseClient):
    URL = "http://www.altopadel.cl/booking/srvc.aspx/"

    HEADERS = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json; charset=UTF-8',
        # 'Cookie': 'ASP.NET_SessionId=52ulrb45b00s2s55mgubaayy; cb-enabled=enabled; i18next=es-CL',
        'Origin': 'http://www.altopadel.cl',
        'Referer': 'http://www.altopadel.cl/Booking/Grid.aspx',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    COOKIES = {
        'ASP.NET_SessionId': '52ulrb45b00s2s55mgubaayy',
        'cb-enabled': 'enabled',
        'i18next': 'es-CL',
    }

    NAME = "Alto Padel"
    FILTER = "Padel"
    P = "eNEe29kXfZCYYTtFPL/1ufji6catFXxwIdkzPGyTWQc="

    @cache_decorator("altopadel", 120, index=1)
    def get_schedule(self, date: str):
        return super().get_schedule(date)
