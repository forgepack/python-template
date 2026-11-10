# _Template Python_

```bash
# create virtual environment
# Windows PowerShell
python -m venv .venv
# Linux
python3 -m venv .venv

# activate virtual environment
.venv/Scripts/activate

# udpate pip
python.exe -m pip install --upgrade pip

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
