<div align="center">

# _Template Python_

[![GitHub stars](https://img.shields.io/github/stars/forgepack/template-python?style=social)](https://github.com/forgepack/template-python)
[![GitHub forks](https://img.shields.io/github/forks/forgepack/template-python?style=social)](https://github.com/forgepack/template-python/fork)
[![GitHub watchers](https://img.shields.io/github/watchers/forgepack/template-python?style=social)](https://github.com/forgepack/template-python)

</div>

## Tech Stack

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115.13-009688?logo=fastapi)

## Endpoints

- `GET /` returns `{"message": "Hello, World!"}`.
- `GET /health` returns `{"status": "healthy"}`.

## Development

This project requires Python 3.13 or later.

```bash
# create virtual environment
# Windows PowerShell
py -3.13 -m venv .venv
# Linux
python3.13 -m venv .venv

# activate virtual environment
# Windows PowerShell
.venv/Scripts/activate
# Linux
source .venv/bin/activate

# update pip
python -m pip install --upgrade pip

# install dependencies
python -m pip install -e ".[dev]"

# run application
python -m app.main
```

## Running Tests

```bash
# test coverage verification
python -m pytest --cov=app --cov-report=term-missing

# test report, in /htmlcov/index.html
python -m pytest --cov=app --cov-report=html

# test execution, with details
python -m pytest -v
```

## DEVELOPERS

### Contributors
> _[Gadelha TI](https://github.com/gadelhati)_ - *Research Software Engineer · Software Architect · Lead Developer*

## LICENSE

This project is licensed under the __MIT License__ - see the [MIT LICENSE](https://choosealicense.com/licenses/mit/) file for details.

```text
MIT License

Copyright (c) 2024 Gadelha TI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

<div align="center">