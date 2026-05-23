# Salary Prediction with Linear Regression

[![CI](https://github.com/itkrivoshei/salary-prediction-linear-regression/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/itkrivoshei/salary-prediction-linear-regression/actions/workflows/ci.yml)
[![Live demo](https://img.shields.io/badge/live%20demo-Streamlit-red)](https://salary-prediction-linear-regression.streamlit.app/)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Docker](https://img.shields.io/badge/docker-build-informational)

A small Streamlit app that trains a linear regression model and predicts salary from years of experience.

## Links

- Live demo: https://salary-prediction-linear-regression.streamlit.app/
- Repository: https://github.com/itkrivoshei/salary-prediction-linear-regression

## What it does

- Loads the included CSV file or accepts an uploaded CSV.
- Validates the required input columns.
- Trains a linear regression model with scikit-learn.
- Shows MSE, RMSE, MAE, and R² metrics.
- Plots actual vs predicted salary values.
- Runs locally, in Docker, or on Streamlit Cloud.

## Tech stack

| Area | Tools |
| --- | --- |
| App | Streamlit |
| Data | Pandas, NumPy |
| Model | scikit-learn |
| Charts | Matplotlib |
| Quality | Ruff, Pytest |
| Runtime | Docker |
| CI | GitHub Actions |

## Repository structure

```text
.
├── streamlit_app.py              # Streamlit Cloud entry point
├── app.py                        # Application UI
├── data/
│   └── salary_data.csv           # Sample dataset
├── src/
│   └── salary_prediction/
│       ├── __init__.py
│       └── model.py              # Data validation and model logic
├── tests/
│   └── test_model.py             # Unit tests
├── .github/workflows/ci.yml      # Lint, test, Docker build
├── .streamlit/config.toml        # Streamlit runtime config
├── .dockerignore
├── .gitignore
├── Dockerfile
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Input format

The CSV file must contain these columns:

| Column | Type | Example |
| --- | --- | --- |
| `experience_years` | number | `5` |
| `salary` | number | `75000` |

Example:

```csv
experience_years,salary
1,42000
3,56000
5,75000
```

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app.py
```

Open:

```text
http://localhost:8501
```

## Run checks

```bash
pip install -e ".[dev]"
ruff check .
pytest
```

## Run with Docker

```bash
docker build -t salary-prediction .
docker run --rm -p 8501:8501 salary-prediction
```

## CI

GitHub Actions runs on `main` pushes and pull requests:

```text
ruff check .
pytest
docker build -t salary-prediction:ci .
```

Workflow file:

```text
.github/workflows/ci.yml
```

## Deployment

Streamlit Cloud entry point:

```text
streamlit_app.py
```

Docker runtime port:

```text
8501
```

## Model note

The model uses one feature: `experience_years`. It is suitable as a simple linear regression example, not as a real salary estimation system.

## License

[MIT](LICENSE)
