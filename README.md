# Salary Prediction Linear Regression

[![Python CI](https://img.shields.io/github/actions/workflow/status/itkrivoshei/salary-prediction-linear-regression/ci.yml?branch=main&style=flat-square)](https://github.com/itkrivoshei/salary-prediction-linear-regression/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/github/license/itkrivoshei/salary-prediction-linear-regression?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.12-blue?style=flat-square&logo=python&logoColor=white)](pyproject.toml)

Streamlit app for salary prediction with linear regression.

Live demo: [salary-prediction-linear-regression.streamlit.app](https://salary-prediction-linear-regression.streamlit.app)

## Project Scope

Small educational ML project for a simple regression workflow: CSV loading, input validation, model training, Streamlit UI, tests, Docker build, Dependabot, and GitHub Actions CI.

The dataset is a small sample CSV stored in the repository. The model should not be used for real compensation benchmarking, hiring decisions, financial planning, or salary negotiation.

## Tech Stack

| Area | Tools |
|---|---|
| Language | Python 3.12 |
| UI | Streamlit |
| Data | pandas, NumPy |
| Machine learning | scikit-learn |
| Visualization | Matplotlib |
| Testing / quality | Pytest, Ruff |
| Container | Docker |
| CI/CD | GitHub Actions |
| Dependency updates | Dependabot |
| Deployment | Streamlit Community Cloud |

## Model

| Item | Value |
|---|---|
| Algorithm | Linear Regression |
| Input feature | Years of experience |
| Target | Salary |
| Dataset source | Local CSV sample |
| Intended use | Educational demo |

## Install

```bash
git clone git@github.com:itkrivoshei/salary-prediction-linear-regression.git
cd salary-prediction-linear-regression
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[app,dev]"
```

## Run

```bash
streamlit run streamlit_app.py
```

Open:

```text
http://localhost:8501
```

## Docker

```bash
docker build -t salary-prediction-linear-regression .
docker run --rm -p 8501:8501 salary-prediction-linear-regression
```

## Verify

Run the same checks used by CI:

```bash
python -m ruff check .
python -m ruff format --check .
python -m pytest -q
python -m compileall -q app.py streamlit_app.py src tests
python -c "import salary_prediction.model"
python -c "import streamlit_app"
```

## CI/CD

GitHub Actions validates dependency installation, Ruff, Pytest, Python compilation, app imports, and Docker image build on pushes and pull requests to `main`.

Dependabot checks Python and GitHub Actions dependencies weekly and is auto-merged after successful CI.

## Project Files

| File | Purpose |
|---|---|
| [`streamlit_app.py`](streamlit_app.py) | Streamlit application entry point |
| [`app.py`](app.py) | Application compatibility entry point |
| [`src/salary_prediction/model.py`](src/salary_prediction/model.py) | Data loading, validation, training, and prediction logic |
| [`data/salary_data.csv`](data/salary_data.csv) | Sample dataset |
| [`tests/test_model.py`](tests/test_model.py) | Unit tests |
| [`Dockerfile`](Dockerfile) | Container image definition |
| [`pyproject.toml`](pyproject.toml) | Project metadata, dependencies, Ruff, and Pytest config |
| [`.github/workflows/ci.yml`](.github/workflows/ci.yml) | CI workflow |
| [`.github/dependabot.yml`](.github/dependabot.yml) | Weekly dependency updates |
| [`LICENSE`](LICENSE) | MIT license |

## Deployment

Streamlit Cloud uses:

```text
Main file path: streamlit_app.py
Python version: runtime.txt
Dependencies: requirements.txt
```

## License

This project is licensed under the [MIT License](LICENSE).
