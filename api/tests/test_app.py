import json
from unittest.mock import patch
from src.app import app

with open("tests/padel_requests/response.json", "rb") as file:
    RESPONSE = json.load(file)


@patch("src.padel_requests.base.requests")
def test_send_reminder(requests, snapshot):
    requests.post().json.return_value = RESPONSE
    data = '{"idCuadro": "4", "fecha": "16/09/2021"}'
    url = "http://www.clubconecta.cl/booking/srvc.aspx/ObtenerCuadro"
    with app.test_client() as test_app:
        result = test_app.get("/get_schedule/conecta/2021-09-16")

    assert requests.post.call_args[0] == (url,)
    assert requests.post.call_args[1].get("headers") is not None
    assert requests.post.call_args[1].get("cookies") is not None
    assert requests.post.call_args[1].get("data") == data
    assert result.status_code == 200
    snapshot.assert_match(result.json)
