import json
import requests

URL = "http://www.clubconecta.cl/booking/srvc.aspx/ObtenerCuadro"


HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.5",
    "Content-Type": "application/json; charset=utf-8",
    "X-Requested-With": "XMLHttpRequest",
    "Origin": "http://www.clubconecta.cl",
    "Connection": "keep-alive",
    "Referer": "http://www.clubconecta.cl/Booking/Grid.aspx",
}

COOKIES = {
    "cb-enabled": "enabled",
    "ASP.NET_SessionId": "cfwfnmn1c15bx0u34g5bkoia",
    "i18next": "es-CL",
}


def get_conecta_schedule(date):
    data = json.dumps({"idCuadro": "4", "fecha": date})  # 16/9/2020
    return requests.post(URL, headers=HEADERS, cookies=COOKIES, data=data).json()
