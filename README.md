# Salary Prediction with Linear Regression

[![CI](https://img.shields.io/github/actions/workflow/status/itkrivoshei/salary-prediction-linear-regression/ci.yml?branch=main&style=flat-square&label=ci)](https://github.com/itkrivoshei/salary-prediction-linear-regression/actions/workflows/ci.yml)
[![Live demo](https://img.shields.io/badge/live%20demo-Streamlit-ff4b4b?style=flat-square)](https://salary-prediction-linear-regression.streamlit.app/)
[![Python](https://img.shields.io/badge/python-3.10%2B-3776ab?style=flat-square)](https://www.python.org/)
[![License](https://img.shields.io/github/license/itkrivoshei/salary-prediction-linear-regression?style=flat-square)](LICENSE)

A small Streamlit app that trains a linear regression model and predicts salary from years of experience.

## Tech stack

| Area | Tools |
| --- | --- |
| App | Streamlit |
| Data | pandas, NumPy |
| Model | scikit-learn |
| Charts | Matplotlib |
| Quality | Ruff, pytest |
| Runtime | Docker, Streamlit Cloud |

## Features

- Loads the included CSV dataset or an uploaded CSV file.
- Validates required input columns.
- Trains a single-feature linear regression model.
- Shows MSE, RMSE, MAE, and R² metrics.
- Displays the fitted model equation and prediction chart.
- Runs locally or in Docker.

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

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

For development checks:

```bash
pip install -e ".[dev]"
```

## Run

```bash
streamlit run streamlit_app.py
```

Open:

```text
http://localhost:8501
```

## Verify

```bash
ruff check .
ruff format --check .
pytest
```

## Docker

```bash
docker build -t salary-prediction .
docker run --rm -p 8501:8501 salary-prediction
```

## Project structure

```text
.
├── app.py
├── streamlit_app.py
├── data/
│   └── salary_data.csv
├── src/
│   └── salary_prediction/
│       ├── __init__.py
│       └── model.py
├── tests/
│   └── test_model.py
├── .github/workflows/ci.yml
├── .streamlit/config.toml
├── Dockerfile
├── pyproject.toml
├── requirements.txt
├── LICENSE
└── README.md
```

## Deployment

Streamlit Cloud entry point:

```text
streamlit_app.py
```

Live demo:

```text
https://salary-prediction-linear-regression.streamlit.app/
```

## Model note

The model uses one feature: `experience_years`. It is a simple regression example, not a real salary benchmark.

## License

[MIT](LICENSE)
