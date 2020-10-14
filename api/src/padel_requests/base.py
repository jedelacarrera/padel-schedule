import json
import requests
from src.helpers import time_to_float


class BaseClient:
    URL = None
    HEADERS = None
    COOKIES = None
    NAME = None
    FILTER = ""
    ID_CUADRO = "4"

    def get_schedule(self, date: str):
        response = requests.post(
            self.URL,
            headers=self.HEADERS,
            cookies=self.COOKIES,
            data=json.dumps({"idCuadro": self.ID_CUADRO, "fecha": date}),  # 16/9/2020
        ).json()

        response = response["d"]

        courts = [
            self.get_info_from_court(
                court, response["StrHoraInicio"], response["StrHoraFin"]
            )
            for court in response["Columnas"]
            if self.FILTER in court.get("TextoPrincipal", "")
        ]
        return {
            "initial_time": response["StrHoraInicio"],
            "initial_time_float": time_to_float(response["StrHoraInicio"]),
            "end_time": response["StrHoraFin"],
            "end_time_float": time_to_float(response["StrHoraFin"]),
            "name": self.NAME,
            "courts": courts,
        }

    @classmethod
    def get_info_from_court(cls, court: dict, initial_time: str, end_time: str) -> dict:
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
        name = court["TextoPrincipal"]
        if "(DOBLES)" in name:
            name = name[:-8].strip()
        return {
            "name": name,
            "provider": cls.NAME,
            "bookings": bookings,
            "fixed_times": fixed_times,
            "initial_time": initial_time,
            "initial_time_float": time_to_float(initial_time),
            "end_time": end_time,
            "end_time_float": time_to_float(end_time),
        }
