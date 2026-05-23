# Salary Prediction with Linear Regression

Simple salary prediction app based on years of experience and a linear regression model.

## Demo

Live demo URL:

```text
https://your-streamlit-app-url
```

For Streamlit Cloud, use this entry point:

```text
app.py
```

## Features

- Load the included sample CSV or upload another dataset.
- Train a linear regression model.
- Show MSE, RMSE, MAE, and R² metrics.
- Plot actual vs predicted salary values.
- Predict salary for a custom experience value.

## Stack

- Python
- Streamlit
- Pandas / NumPy
- scikit-learn
- Matplotlib
- Pytest / Ruff
- Docker
- GitHub Actions

## Structure

```text
.
├── app.py
├── data/
│   └── salary_data.csv
├── src/
│   └── salary_prediction/
│       ├── __init__.py
│       └── model.py
├── tests/
│   └── test_model.py
├── .github/workflows/ci.yml
├── Dockerfile
├── pyproject.toml
├── requirements.txt
└── README.md
```

## CSV format

```csv
experience_years,salary
1,42000
3,56000
5,75000
```

Required columns:

| Column | Description |
| --- | --- |
| `experience_years` | Years of professional experience |
| `salary` | Salary value |

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
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

Open:

```text
http://localhost:8501
```

## Notes

This is a small linear regression example. The model uses only one feature, so predictions are easy to inspect but not suitable for real salary estimation.

## License

MIT
