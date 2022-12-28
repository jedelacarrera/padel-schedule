from src.padel_requests.base import BaseClient
from src.memoization_decorator import cache_decorator


class PadelOriente(BaseClient):
    URL = "http://padeloriente.cl/booking/srvc.aspx/"

    HEADERS = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json; charset=UTF-8",
        # 'Cookie': 'ASP.NET_SessionId=hd4wmv45icl3gorj222wt0ip; cb-enabled=enabled; i18next=es-CL',
        "Origin": "http://padeloriente.cl",
        "Referer": "http://padeloriente.cl/Booking/Grid.aspx",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",  # pylint: disable=line-too-long
        "X-Requested-With": "XMLHttpRequest",
    }

    COOKIES = {
        "ASP.NET_SessionId": "hd4wmv45icl3gorj222wt0ip",
        "cb-enabled": "enabled",
        "i18next": "es-CL",
    }

    NAME = "Padel Oriente"
    FILTER = "Cancha"
    P = "eNEe29kXfZCYYTtFPL/1ufQZK/cQ2h54tlxxm4VoJ34="

    @cache_decorator("padeloriente", 120, index=1)
    def get_schedule(self, date: str):
        result = super().get_schedule(date)
        return result
