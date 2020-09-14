import re
from src.padel_requests.conecta import get_conecta_schedule

# REGEX = r"^[0-3]?[0-9][/-\.][01]?[0-9][/-\.]202[0-9]$"
REGEX = re.compile(r"^(202[0-9]).([01]?[0-9]).([0123]?[0-9])$")


PADEL_REQUESTS = {
  "conecta": get_conecta_schedule,
  "padelbreak": get_conecta_schedule,
}

def map_date(date):
  result = REGEX.match(date)
  year = result.group(1)
  month = result.group(2)
  day = result.group(3)
  if len(month) == 1:
    month = '0' + month

  if len(day) == 1:
    day = '0' + day

  return f"{day}-{month}-{year}"
