import re
from src.padel_requests.conecta import ConectaClient
from src.padel_requests.padelbreak import PadelBreakClient
from src.padel_requests.santuario import SantuarioClient
from src.padel_requests.bullpadel import BullPadelClient
from src.padel_requests.padeloriente import PadelOriente
from src.padel_requests.altopadel import AltoPadelClient
from src.padel_requests.maspadel import MasPadelClient
from src.padel_requests.rinconada import Rinconada
from src.padel_requests.redpadel import RedPadelClient

REGEX = re.compile(r"^(202[0-9]).([01]?[0-9]).([0123]?[0-9])$")


PADEL_REQUESTS = {
    "conecta": ConectaClient(),
    "padelbreak": PadelBreakClient(),
    "santuario": SantuarioClient(),
    "bullpadel": BullPadelClient(),
    "padeloriente": PadelOriente(),
    "altopadel": AltoPadelClient(),
    "maspadel": MasPadelClient(),
    "rinconada": Rinconada(),
    "redpadel": RedPadelClient(),
}


def map_date(date):
    result = REGEX.match(date)
    year = result.group(1)
    month = result.group(2)
    day = result.group(3)
    if len(month) == 1:
        month = "0" + month

    if len(day) == 1:
        day = "0" + day

    return f"{day}/{month}/{year}"
