from src.padel_requests.base import BaseClient
from src.memoization_decorator import cache_decorator


class ConectaClient(BaseClient):
    URL = "https://www.clubconecta.cl/booking/srvc.aspx/"

    HEADERS = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json; charset=UTF-8',
        # 'Cookie': 'ASP.NET_SessionId=x5s4gcjdqfbyg3450m2ht055; _fbp=fb.1.1672196038024.1226051803; _ga=GA1.2.1094118402.1672196039; _gid=GA1.2.235286405.1672196039; _gat_gtag_UA_225409570_1=1; i18next=es-CL',  # pylint: disable=line-too-long
        'Origin': 'https://www.clubconecta.cl',
        'Referer': 'https://www.clubconecta.cl/Pages/15-CLUB_CONECTA_LA_DEHESA_PADEL',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',  # pylint: disable=line-too-long
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    COOKIES = {
        'ASP.NET_SessionId': 'x5s4gcjdqfbyg3450m2ht055',
        '_fbp': 'fb.1.1672196038024.1226051803',
        '_ga': 'GA1.2.1094118402.1672196039',
        '_gid': 'GA1.2.235286405.1672196039',
        '_gat_gtag_UA_225409570_1': '1',
        'i18next': 'es-CL',
    }

    NAME = "Conecta"
    FILTER = "Pádel"
    ID_CUADRO = "5"
    P = "eNEe29kXfZDAz5z94mPqWy9Q9mCzyGFZyiJh+wMWWunglvloaKL4JA=="

    @cache_decorator("conecta", 120, index=1)
    def get_schedule(self, date: str):
        return super().get_schedule(date)
