# Salary Prediction Linear Regression

[![Python CI](https://img.shields.io/github/actions/workflow/status/itkrivoshei/salary-prediction-linear-regression/ci.yml?branch=main&style=flat-square)](https://github.com/itkrivoshei/salary-prediction-linear-regression/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/github/license/itkrivoshei/salary-prediction-linear-regression?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.12-blue?style=flat-square&logo=python&logoColor=white)](pyproject.toml)

Streamlit app for salary prediction with linear regression.

Live demo: [salary-prediction-linear-regression.streamlit.app](https://salary-prediction-linear-regression.streamlit.app)

## Project Scope

This is a small educational ML project. It demonstrates CSV data loading, input validation, linear regression training, Streamlit UI, tests, linting, Docker build, Dependabot updates, and GitHub Actions CI.

The dataset is a small sample CSV stored in the repository. The model should not be used for real compensation benchmarking, hiring decisions, financial planning, or salary negotiation.

## Features

- Load salary data from CSV
- Validate required dataset columns and input values
- Train a linear regression model with scikit-learn
- Predict salary from years of experience
- Display the workflow through Streamlit
- Validate the project with Pytest and Ruff
- Build the app as a Docker image

## Tech Stack

| Area | Tools |
|---|---|
| Language | Python 3.12 |
| UI | Streamlit |
| Data | pandas, NumPy |
| Machine learning | scikit-learn |
| Visualization | Matplotlib |
| Testing | Pytest |
| Linting / formatting | Ruff |
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

Clone the repository:

```bash
git clone git@github.com:itkrivoshei/salary-prediction-linear-regression.git
cd salary-prediction-linear-regression
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[app,dev]"
```

## Run

Run the Streamlit app:

```bash
streamlit run streamlit_app.py
```

Open:

```text
http://localhost:8501
```

## Docker

Build and run the container:

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

The GitHub Actions workflow validates dependency installation, Ruff, Pytest, Python compilation, app imports, and Docker image build on pushes and pull requests to `main`.

Dependabot checks Python and GitHub Actions dependencies weekly. Dependabot pull requests are automatically squash-merged after successful CI.

## Project Structure

```text
.
├── .github/
│   ├── dependabot.yml
│   └── workflows/
│       ├── ci.yml
│       └── dependabot-auto-merge.yml
├── .streamlit/
│   └── config.toml
├── data/
│   └── salary_data.csv
├── src/
│   └── salary_prediction/
│       ├── __init__.py
│       └── model.py
├── tests/
│   └── test_model.py
├── app.py
├── streamlit_app.py
├── Dockerfile
├── requirements.txt
├── runtime.txt
├── pyproject.toml
└── README.md
```

## Key Files

| File | Purpose |
|---|---|
| [`streamlit_app.py`](streamlit_app.py) | Streamlit application entry point |
| [`app.py`](app.py) | Application compatibility entry point |
| [`src/salary_prediction/model.py`](src/salary_prediction/model.py) | Data loading, validation, training, and prediction logic |
| [`data/salary_data.csv`](data/salary_data.csv) | Small sample dataset |
| [`tests/test_model.py`](tests/test_model.py) | Unit tests |
| [`Dockerfile`](Dockerfile) | Container image definition |
| [`requirements.txt`](requirements.txt) | Streamlit Cloud dependency entry point |
| [`runtime.txt`](runtime.txt) | Python runtime version for Streamlit Cloud |
| [`pyproject.toml`](pyproject.toml) | Project metadata, dependency ranges, Ruff, and Pytest config |
| [`.streamlit/config.toml`](.streamlit/config.toml) | Streamlit app configuration |
| [`.github/workflows/ci.yml`](.github/workflows/ci.yml) | CI workflow |
| [`.github/workflows/dependabot-auto-merge.yml`](.github/workflows/dependabot-auto-merge.yml) | Dependabot auto-merge after green CI |
| [`.github/dependabot.yml`](.github/dependabot.yml) | Weekly dependency update checks |
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
