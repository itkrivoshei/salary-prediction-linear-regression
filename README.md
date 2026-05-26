<div align="center">

# Salary Prediction Linear Regression

Single-feature salary prediction app with Streamlit, pandas, scikit-learn, tests, and a Docker image.

[![Live app](https://img.shields.io/badge/live-Streamlit-ff4b4b?style=for-the-badge&logo=streamlit&logoColor=white)](https://salary-prediction-linear-regression.streamlit.app/)
[![Python CI](https://img.shields.io/github/actions/workflow/status/itkrivoshei/salary-prediction-linear-regression/ci.yml?branch=main&style=for-the-badge&label=ci&logo=githubactions&logoColor=white)](https://github.com/itkrivoshei/salary-prediction-linear-regression/actions/workflows/ci.yml)
[![Docker](https://img.shields.io/badge/Docker-ready-2496ed?style=for-the-badge&logo=docker&logoColor=white)](Dockerfile)
[![License](https://img.shields.io/github/license/itkrivoshei/salary-prediction-linear-regression?style=for-the-badge)](LICENSE)

### [Open Streamlit App ->](https://salary-prediction-linear-regression.streamlit.app/)

</div>

## What The App Does

Upload a CSV or use the bundled `data/salary_data.csv`, train a linear regression model, inspect metrics, view the fitted line, and estimate salary from years of professional experience.

Expected CSV shape:

```text
experience_years,salary
1,42000
3,56000
```

## Model Contract

| Item | Value |
| --- | --- |
| Algorithm | Linear Regression |
| Feature | `experience_years` |
| Target | `salary` |
| Validation | Required columns, numeric coercion, minimum row count, positive salary values |
| Metrics | MSE, RMSE, MAE, R2 |

The model uses one input feature and should not be used for compensation benchmarking, hiring decisions, financial planning, or salary negotiation.

## Local Setup

```bash
git clone https://github.com/itkrivoshei/salary-prediction-linear-regression.git
cd salary-prediction-linear-regression
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[app,dev]"
streamlit run streamlit_app.py
```

Open `http://localhost:8501`.

## Docker

```bash
docker build -t salary-prediction-linear-regression .
docker run --rm -p 8501:8501 salary-prediction-linear-regression
```

## Verification

| Command | Purpose |
| --- | --- |
| `python -m ruff check .` | Lint Python files |
| `python -m ruff format --check .` | Check formatting |
| `python -m pytest -q` | Run tests |
| `python -m compileall -q app.py streamlit_app.py src tests` | Compile modules |
| `python -c "import salary_prediction.model"` | Validate package import |
| `python -c "import streamlit_app"` | Validate app import |

CI also builds the Docker image.

## Key Files

```text
app.py                         # Streamlit UI
streamlit_app.py               # Streamlit Cloud entry point
src/salary_prediction/model.py # loading, validation, training, prediction
data/salary_data.csv           # bundled CSV sample
tests/test_model.py            # model tests
Dockerfile                     # production container
```

Live app: https://salary-prediction-linear-regression.streamlit.app/

## License

[MIT](LICENSE)
