import json
import requests
from src.helpers import time_to_float
from src.memoization_decorator import cache_decorator

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


@cache_decorator("conecta", 60)
def get_conecta_schedule(date: str) -> dict:
    data = json.dumps({"idCuadro": "4", "fecha": date})  # 16/9/2020
    response = requests.post(URL, headers=HEADERS, cookies=COOKIES, data=data).json()
    response = response["d"]
    courts = [
        get_info_from_court(court)
        for court in response["Columnas"]
        if court.get("TextoSecundario") == "Pádel"
        or "Pádel" in court.get("TextoPrincipal", "")
    ]
    return {
        "initial_time": response["StrHoraInicio"],
        "initial_time_float": time_to_float(response["StrHoraInicio"]),
        "end_time": response["StrHoraFin"],
        "end_time_float": time_to_float(response["StrHoraFin"]),
        "name": response["Nombre"],
        "courts": courts,
    }


def get_info_from_court(court: dict) -> dict:
    bookings = [
        {
            "initial_time": booking["StrHoraInicio"],
            "initial_time_float": time_to_float(booking["StrHoraInicio"]),
            "end_time": booking["StrHoraFin"],
            "end_time_float": time_to_float(booking["StrHoraFin"]),
            "total_time": booking["Minutos"],
        }
        for booking in court["Ocupaciones"]
    ]
    bookings.sort(key=lambda x: x["initial_time"])
    fixed_times = [
        {
            "initial_time": fixed_time["StrHoraInicio"],
            "initial_time_float": time_to_float(fixed_time["StrHoraInicio"]),
            "end_time": fixed_time["StrHoraFin"],
            "end_time_float": time_to_float(fixed_time["StrHoraFin"]),
            "total_time": fixed_time["Minutos"],
            "valid": fixed_time["Clickable"],
        }
        for fixed_time in court["HorariosFijos"]
    ]
    fixed_times.sort(key=lambda x: x["initial_time"])
    return {
        "name": court["TextoPrincipal"],
        "provider": "Conecta",
        "bookings": bookings,
        "fixed_times": fixed_times,
    }
