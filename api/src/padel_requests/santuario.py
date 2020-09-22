from src.padel_requests.base import BaseClient
from src.memoization_decorator import cache_decorator


class SantuarioClient(BaseClient):
    URL = "https://clubsantuariodelvalle.matchpoint.com.es/booking/srvc.aspx/ObtenerCuadro"

    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",  # pylint: disable=line-too-long
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/json; charset=utf-8",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://clubsantuariodelvalle.matchpoint.com.es",
        "DNT": "1",
        "Connection": "keep-alive",
        "Referer": "https://clubsantuariodelvalle.matchpoint.com.es/Booking/Grid.aspx",
        "TE": "Trailers",
    }

    COOKIES = {
        "ASP.NET_SessionId": "vpoccb45t3dmwb55tc5zhlq3",
        "cb-enabled": "enabled",
        "i18next": "es-CL",
    }

    NAME = "Santuario"
    FILTER = "Padel"

    @cache_decorator("santuario", 60, index=1)
    def get_schedule(self, date: str):
        result = super().get_schedule(date)
        return result
