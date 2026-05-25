# Salary Prediction Linear Regression

[![Python CI](https://img.shields.io/github/actions/workflow/status/itkrivoshei/salary-prediction-linear-regression/ci.yml?branch=main&style=flat-square)](https://github.com/itkrivoshei/salary-prediction-linear-regression/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/github/license/itkrivoshei/salary-prediction-linear-regression?style=flat-square)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.12-blue?style=flat-square&logo=python&logoColor=white)](pyproject.toml)

Streamlit app for salary prediction with linear regression.

The project demonstrates a compact Python machine-learning workflow: CSV data loading, input validation, linear regression training, prediction, Streamlit UI, tests, linting, formatting checks, Docker build, and GitHub Actions CI.

## Project Status

This is a small educational ML project. It is useful for demonstrating a basic regression workflow, but it should not be used for real compensation benchmarking, hiring decisions, financial planning, or salary negotiation.

The dataset is a small sample CSV stored in the repository. The model is intentionally simple and focuses on project structure, validation, reproducibility, and delivery workflow rather than production-grade salary modelling.

## Features

- Load salary data from CSV
- Validate required dataset columns and input values
- Train a linear regression model with scikit-learn
- Predict salary from years of experience
- Display the workflow through Streamlit
- Validate the project with Pytest and Ruff
- Build the app as a Docker image
- Run automated checks with GitHub Actions

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
| CI | GitHub Actions |
| Dependency checks | Dependabot |

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

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
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

The app runs locally at:

```text
http://localhost:8501
```

## Docker

Build the image:

```bash
docker build -t salary-prediction-linear-regression .
```

Run the container:

```bash
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

The GitHub Actions workflow runs on pushes and pull requests to `main`.

It checks:

- dependency installation
- Ruff linting
- Ruff formatting
- Pytest tests
- Python module compilation
- package import
- Streamlit app import
- Docker image build

Dependabot checks Python and GitHub Actions dependencies weekly. Major version updates are ignored by default and should be reviewed manually.

## Project Structure

```text
.
├── .github/
│   ├── dependabot.yml
│   └── workflows/
│       └── ci.yml
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
| `streamlit_app.py` | Streamlit application entry point |
| `app.py` | Application compatibility entry point |
| `src/salary_prediction/model.py` | Data loading, validation, training, and prediction logic |
| `data/salary_data.csv` | Small sample dataset |
| `tests/test_model.py` | Unit tests for data and model behavior |
| `Dockerfile` | Container image definition |
| `.github/workflows/ci.yml` | CI validation |
| `.github/dependabot.yml` | Weekly dependency update checks |

## Streamlit Cloud Setup

Use these settings if deploying the app to Streamlit Community Cloud:

```text
Main file path: streamlit_app.py
Python version: runtime.txt
Dependencies: requirements.txt
```

`requirements.txt` installs the package with app dependencies:

```text
-e .[app]
```

## License

This project is licensed under the [MIT License](LICENSE).
