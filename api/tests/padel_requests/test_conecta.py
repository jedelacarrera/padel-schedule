import json
from unittest.mock import patch
from src.padel_requests.conecta import get_info_from_court, get_conecta_schedule

with open("tests/padel_requests/response.json", "rb") as file:
    RESPONSE = json.load(file)


def test_get_info_from_court(snapshot):
    result = get_info_from_court(RESPONSE["d"]["Columnas"][4])
    snapshot.assert_match(result)


@patch("src.padel_requests.conecta.requests")
def test_get_conecta_schedule(requests, snapshot):
    requests.post().json.return_value = RESPONSE
    data = '{"idCuadro": "4", "fecha": "16/09/2021"}'
    url = "http://www.clubconecta.cl/booking/srvc.aspx/ObtenerCuadro"
    result = get_conecta_schedule("16/09/2021")
    assert requests.post.call_args[0] == (url,)
    assert requests.post.call_args[1].get("headers") is not None
    assert requests.post.call_args[1].get("cookies") is not None
    assert requests.post.call_args[1].get("data") == data
    snapshot.assert_match(result)
