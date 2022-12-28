# API

## Commands

  source venv/bin/activate;
  export $(grep -v '^#' .env | xargs);
  code .;
  python -m pip install -q -r requirements.txt;

### Run
    python -m flask run --host=0.0.0.0 --port=8000;

### Tests

```
python -m pylint src tests;
python -m black --check src tests --exclude "/snapshots/";
python -m pytest -vv --disable-warnings;
```
