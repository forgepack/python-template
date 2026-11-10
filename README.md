# _Template Python_

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.13-009688?logo=fastapi)

## Endpoints

- `GET /` returns `{"message": "Hello, World!"}`.
- `GET /health` returns `{"status": "healthy"}`.

## Development

```bash
# create virtual environment
# Windows PowerShell
python -m venv .venv
# Linux
python3 -m venv .venv

# activate virtual environment
# Windows PowerShell
.venv/Scripts/activate
# Linux
source .venv/bin/activate

# update pip
python -m pip install --upgrade pip

# install dependencies
pip install -e ".[dev]"

# run application
python -m app.main

# test coverage verification
python -m pytest --cov=app --cov-report=term-missing

# test report, in /htmlcov/index.html
python -m pytest --cov=app --cov-report=html

# test execution, with details
python -m pytest -v
```
