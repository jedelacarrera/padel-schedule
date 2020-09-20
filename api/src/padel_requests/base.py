import json
import requests
from src.helpers import time_to_float


class BaseClient:
    URL = None
    HEADERS = None
    COOKIES = None
    NAME = None

    def get_schedule(self, date: str):
        response = requests.post(
            self.URL,
            headers=self.HEADERS,
            cookies=self.COOKIES,
            data=json.dumps({"idCuadro": "4", "fecha": date}),  # 16/9/2020
        ).json()

        response = response["d"]
        courts = [
            self.get_info_from_court(court)
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

    @staticmethod
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
