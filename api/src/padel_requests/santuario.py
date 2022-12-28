from src.padel_requests.base import BaseClient
from src.memoization_decorator import cache_decorator


class SantuarioClient(BaseClient):
    URL = "https://www.tenissantuario.cl/booking/srvc.aspx/"

    HEADERS = {
        "authority": "www.tenissantuario.cl",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "en-US,en;q=0.9",
        "content-type": "application/json; charset=UTF-8",
        # 'cookie': 'ASP.NET_SessionId=w0mz2neov344ks55ptntwwuy; cb-enabled=enabled; i18next=es-CL',
        "origin": "https://www.tenissantuario.cl",
        "referer": "https://www.tenissantuario.cl/Booking/Grid.aspx",
        "sec-ch-ua": '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",  # pylint: disable=line-too-long
        "x-requested-with": "XMLHttpRequest",
    }

    COOKIES = {
        "ASP.NET_SessionId": "w0mz2neov344ks55ptntwwuy",
        "cb-enabled": "enabled",
        "i18next": "es-CL",
    }

    NAME = "Santuario"
    FILTER = "Padel"
    P = "eNEe29kXfZDAz5z94mPqW3jB3ITnAo0ZGhL4FFF23XjglvloaKL4JA=="

    @cache_decorator("santuario", 60, index=1)
    def get_schedule(self, date: str):
        result = super().get_schedule(date)
        return result
