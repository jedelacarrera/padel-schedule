import json
import logging
import requests

from google.cloud.logging import Client as LoggingClient
from src.helpers import time_to_float

logging_info = {"setup": False, "client": None}


def send_warning(info):
    if logging_info["client"] is None:

        logging_info["client"] = LoggingClient()
        logging_info["client"].setup_logging()

    logging.warning(info)


class BaseClient:
    URL = "None"
    HEADERS = None
    COOKIES = None
    NAME = None
    FILTER = ""
    ID_CUADRO = "4"
    DEFAULT_START_TIME = "07:00"  # Just in case it is needed
    DEFAULT_END_TIME = "23:00"  # Just in case it is needed
    P = None

    def get_availability(self, resource: str, date: str, hour: str) -> dict:
        data = json.dumps(
            {
                "idCuadro": self.ID_CUADRO,
                "idRecurso": resource,
                "idmodalidad": 5,
                "fecha": date,  # 28/11/2020
                "hora": hour,  # 13:30
            }
        )
        response = requests.post(
            self.URL + "ObtenerInformacionHuecoLibre",
            headers=self.HEADERS,
            cookies=self.COOKIES,
            data=data,
        ).json()
        return {
            "title": response["d"]["Titulo"],
            "image_url": response["d"]["Url_Imagen"],
            "options": [
                {"token": option["Token"], "description": option["Descripcion"]}
                for option in response["d"]["Opciones"]
            ],
        }

    def get_fixed_time_info(self, resource: str, date: str, hour: int) -> dict:
        data = json.dumps(
            {
                "id": resource,  # "15"
                "idmodalidad": 3,
                "fecha": date,  # "28/11/2020"
                "idHorario": hour,  # 1134
            }
        )
        response = requests.post(
            self.URL + "ObtenerInformacionHorarioPrefijadoLibre",
            headers=self.HEADERS,
            cookies=self.COOKIES,
            data=data,
        ).json()
        return {
            "title": response["d"]["Titulo"],
            "image_url": response["d"]["Url_Imagen"],
            "options": [
                {"token": option["Token"], "description": option["Descripcion"]}
                for option in response["d"]["Opciones"]
            ],
        }

    def get_schedule(self, date: str):
        print("Getting schedule for", date)
        print(self.URL + "ObtenerCuadro")
        print(self.HEADERS)
        print(self.COOKIES)
        print(json.dumps({"idCuadro": self.ID_CUADRO, "fecha": date, "p": self.P}))

        response = requests.post(
            self.URL + "ObtenerCuadro",
            headers=self.HEADERS,
            cookies=self.COOKIES,
            data=json.dumps({"idCuadro": self.ID_CUADRO, "fecha": date, "p": self.P}),  # 16/9/2020
        ).json()
        print(response)

        response = response["d"]

        # Sometimes it is None
        response["StrHoraInicio"] = response["StrHoraInicio"] or self.DEFAULT_START_TIME
        response["StrHoraFin"] = response["StrHoraFin"] or self.DEFAULT_END_TIME

        courts = [
            self.get_info_from_court(
                court, response["StrHoraInicio"], response["StrHoraFin"]
            )
            for court in response["Columnas"]
            if self.FILTER in court.get("TextoPrincipal", "")
        ]
        if len(courts) == 0:
            logging.warning(response)

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
                "id": fixed_time["Id"],
                "initial_time": fixed_time["StrHoraInicio"],
                "initial_time_float": time_to_float(fixed_time["StrHoraInicio"]),
                "end_time": fixed_time["StrHoraFin"],
                "end_time_float": time_to_float(fixed_time["StrHoraFin"]),
                "total_time": fixed_time["Minutos"],
                "valid": fixed_time["Clickable"],
                "price": fixed_time.get("TextoAdicional", ""),
            }
            for fixed_time in court["HorariosFijos"]
        ]
        fixed_times.sort(key=lambda x: x["initial_time"])
        name = court["TextoPrincipal"]
        if "(DOBLES)" in name:
            name = name[:-8].strip()
        return {
            "id": court["Id"],
            "name": name,
            "provider": cls.NAME,
            "bookings": bookings,
            "fixed_times": fixed_times,
            "initial_time": initial_time,
            "initial_time_float": time_to_float(initial_time),
            "end_time": end_time,
            "end_time_float": time_to_float(end_time),
        }
