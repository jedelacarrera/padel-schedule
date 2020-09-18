import json
from unittest.mock import patch
from src.padel_requests.conecta import get_info_from_court, get_conecta_schedule

with open("tests/padel_requests/response.json", "rb") as file:
    RESPONSE = json.load(file)


def test_get_info_from_court():
    result = get_info_from_court(RESPONSE["d"]["Columnas"][4])
    assert result == {
        "bookings": [
            {"end_time": "10:30", "initial_time": "09:00", "total_time": 90},
            {"end_time": "19:30", "initial_time": "18:00", "total_time": 90},
            {"end_time": "21:00", "initial_time": "19:30", "total_time": 90},
            {"end_time": "22:00", "initial_time": "21:00", "total_time": 60},
        ],
        "fixed_times": [
            {
                "end_time": "12:00",
                "initial_time": "10:30",
                "total_time": 90,
                "valid": True,
            },
            {
                "end_time": "13:30",
                "initial_time": "12:00",
                "total_time": 90,
                "valid": True,
            },
            {
                "end_time": "15:00",
                "initial_time": "13:30",
                "total_time": 90,
                "valid": True,
            },
            {
                "end_time": "16:30",
                "initial_time": "15:00",
                "total_time": 90,
                "valid": True,
            },
            {
                "end_time": "18:00",
                "initial_time": "16:30",
                "total_time": 90,
                "valid": True,
            },
        ],
        "name": "Pádel 1",
    }


@patch("src.padel_requests.conecta.requests")
def test_get_conecta_schedule(requests):
    requests.post().json.return_value = RESPONSE
    data = '{"idCuadro": "4", "fecha": "16/09/2021"}'
    url = "http://www.clubconecta.cl/booking/srvc.aspx/ObtenerCuadro"
    result = get_conecta_schedule("16/09/2021")
    assert requests.post.call_args[0] == (url,)
    assert requests.post.call_args[1].get("headers") is not None
    assert requests.post.call_args[1].get("cookies") is not None
    assert requests.post.call_args[1].get("data") == data
    assert result == {
        "courts": [
            {
                "bookings": [
                    {"end_time": "10:30", "initial_time": "09:00", "total_time": 90},
                    {"end_time": "19:30", "initial_time": "18:00", "total_time": 90},
                    {"end_time": "21:00", "initial_time": "19:30", "total_time": 90},
                    {"end_time": "22:00", "initial_time": "21:00", "total_time": 60},
                ],
                "fixed_times": [
                    {
                        "end_time": "12:00",
                        "initial_time": "10:30",
                        "total_time": 90,
                        "valid": True,
                    },
                    {
                        "end_time": "13:30",
                        "initial_time": "12:00",
                        "total_time": 90,
                        "valid": True,
                    },
                    {
                        "end_time": "15:00",
                        "initial_time": "13:30",
                        "total_time": 90,
                        "valid": True,
                    },
                    {
                        "end_time": "16:30",
                        "initial_time": "15:00",
                        "total_time": 90,
                        "valid": True,
                    },
                    {
                        "end_time": "18:00",
                        "initial_time": "16:30",
                        "total_time": 90,
                        "valid": True,
                    },
                ],
                "name": "Pádel 1",
            },
            {
                "bookings": [
                    {"end_time": "20:00", "initial_time": "09:30", "total_time": 630}
                ],
                "fixed_times": [
                    {
                        "end_time": "11:00",
                        "initial_time": "09:30",
                        "total_time": 90,
                        "valid": False,
                    },
                    {
                        "end_time": "12:30",
                        "initial_time": "11:00",
                        "total_time": 90,
                        "valid": False,
                    },
                    {
                        "end_time": "14:00",
                        "initial_time": "12:30",
                        "total_time": 90,
                        "valid": False,
                    },
                    {
                        "end_time": "15:30",
                        "initial_time": "14:00",
                        "total_time": 90,
                        "valid": False,
                    },
                    {
                        "end_time": "17:00",
                        "initial_time": "15:30",
                        "total_time": 90,
                        "valid": False,
                    },
                    {
                        "end_time": "18:30",
                        "initial_time": "17:00",
                        "total_time": 90,
                        "valid": False,
                    },
                    {
                        "end_time": "20:00",
                        "initial_time": "18:30",
                        "total_time": 90,
                        "valid": False,
                    },
                ],
                "name": "Pádel 2",
            },
            {
                "bookings": [
                    {"end_time": "10:30", "initial_time": "09:00", "total_time": 90},
                    {"end_time": "21:00", "initial_time": "19:30", "total_time": 90},
                    {"end_time": "22:00", "initial_time": "21:00", "total_time": 60},
                ],
                "fixed_times": [
                    {
                        "end_time": "12:00",
                        "initial_time": "10:30",
                        "total_time": 90,
                        "valid": True,
                    },
                    {
                        "end_time": "13:30",
                        "initial_time": "12:00",
                        "total_time": 90,
                        "valid": True,
                    },
                    {
                        "end_time": "15:00",
                        "initial_time": "13:30",
                        "total_time": 90,
                        "valid": True,
                    },
                    {
                        "end_time": "16:30",
                        "initial_time": "15:00",
                        "total_time": 90,
                        "valid": True,
                    },
                    {
                        "end_time": "18:00",
                        "initial_time": "16:30",
                        "total_time": 90,
                        "valid": True,
                    },
                    {
                        "end_time": "19:30",
                        "initial_time": "18:00",
                        "total_time": 90,
                        "valid": True,
                    },
                ],
                "name": "Pádel 3",
            },
            {
                "bookings": [
                    {"end_time": "20:00", "initial_time": "09:30", "total_time": 630}
                ],
                "fixed_times": [
                    {
                        "end_time": "11:00",
                        "initial_time": "09:30",
                        "total_time": 90,
                        "valid": False,
                    },
                    {
                        "end_time": "12:30",
                        "initial_time": "11:00",
                        "total_time": 90,
                        "valid": False,
                    },
                    {
                        "end_time": "14:00",
                        "initial_time": "12:30",
                        "total_time": 90,
                        "valid": False,
                    },
                    {
                        "end_time": "15:30",
                        "initial_time": "14:00",
                        "total_time": 90,
                        "valid": False,
                    },
                    {
                        "end_time": "17:00",
                        "initial_time": "15:30",
                        "total_time": 90,
                        "valid": False,
                    },
                    {
                        "end_time": "18:30",
                        "initial_time": "17:00",
                        "total_time": 90,
                        "valid": False,
                    },
                    {
                        "end_time": "20:00",
                        "initial_time": "18:30",
                        "total_time": 90,
                        "valid": False,
                    },
                ],
                "name": "Pádel 4",
            },
            {
                "bookings": [
                    {"end_time": "10:00", "initial_time": "09:00", "total_time": 60},
                    {"end_time": "14:00", "initial_time": "10:00", "total_time": 240},
                    {"end_time": "15:00", "initial_time": "14:00", "total_time": 60},
                    {"end_time": "23:00", "initial_time": "15:00", "total_time": 480},
                ],
                "fixed_times": [
                    {
                        "end_time": "10:30",
                        "initial_time": "09:00",
                        "total_time": 90,
                        "valid": False,
                    },
                    {
                        "end_time": "12:00",
                        "initial_time": "10:30",
                        "total_time": 90,
                        "valid": False,
                    },
                    {
                        "end_time": "13:30",
                        "initial_time": "12:00",
                        "total_time": 90,
                        "valid": False,
                    },
                    {
                        "end_time": "15:00",
                        "initial_time": "13:30",
                        "total_time": 90,
                        "valid": False,
                    },
                    {
                        "end_time": "16:30",
                        "initial_time": "15:00",
                        "total_time": 90,
                        "valid": False,
                    },
                    {
                        "end_time": "18:00",
                        "initial_time": "16:30",
                        "total_time": 90,
                        "valid": False,
                    },
                    {
                        "end_time": "19:30",
                        "initial_time": "18:00",
                        "total_time": 90,
                        "valid": False,
                    },
                    {
                        "end_time": "21:00",
                        "initial_time": "19:30",
                        "total_time": 90,
                        "valid": False,
                    },
                    {
                        "end_time": "22:00",
                        "initial_time": "21:00",
                        "total_time": 60,
                        "valid": False,
                    },
                ],
                "name": "Pádel 5",
            },
        ],
        "end_time": "23:00",
        "initial_time": "09:00",
        "name": "Club Conecta",
    }
