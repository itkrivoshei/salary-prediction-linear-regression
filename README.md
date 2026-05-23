# Salary Prediction with Linear Regression

A small, production-style machine learning project that predicts salary from years of professional experience using a linear regression model.

The project was modernized from a local Tkinter prototype into a browser-based Streamlit application with a cleaner Python structure, reproducible setup, tests, linting, Docker support, and GitHub Actions CI.

## Live demo

Deploy this repository on Streamlit Community Cloud using:

```text
app.py
```

After deployment, add the live app URL here:

```text
https://your-streamlit-app-url
```

## Preview

The application allows users to:

- upload a CSV dataset or use the included sample dataset;
- train a linear regression model;
- review model metrics such as MSE, RMSE, MAE, and R²;
- visualize actual vs predicted salaries;
- make a salary prediction for a custom experience value.

## Tech stack

| Area | Tools |
| --- | --- |
| Language | Python |
| Web app | Streamlit |
| Data | Pandas, NumPy |
| Machine learning | scikit-learn |
| Visualization | Matplotlib |
| Quality | Ruff, Pytest |
| DevOps | GitHub Actions, Docker |

## Project structure

```text
.
├── app.py                         # Streamlit web application
├── src/
│   └── salary_prediction/
│       ├── __init__.py
│       └── model.py               # Data validation, training, prediction helpers
├── data/
│   └── salary_data.csv            # Small sample dataset
├── tests/
│   └── test_model.py              # Unit tests for model logic
├── .github/
│   └── workflows/
│       └── ci.yml                 # Lint and test workflow
├── Dockerfile                     # Containerized app runtime
├── pyproject.toml                 # Project metadata and tool configuration
├── requirements.txt               # Runtime dependencies for Streamlit Cloud
└── README.md
```

## Dataset format

The application expects a CSV file with these columns:

| Column | Type | Example |
| --- | --- | --- |
| `experience_years` | number | `5` |
| `salary` | number | `75000` |

The previous dataset contained unrelated personal-style columns such as names, emails, and phone numbers. The modernized version keeps only the two fields needed for the regression task.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## Run tests and linting

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

## Model notes

This is intentionally a simple baseline model. Linear regression is useful here because the relationship is easy to explain and visualize. For a larger real-world salary prediction system, more features would be needed, such as role, location, seniority, education, industry, and company size.

## Repository modernization checklist

- [x] Replaced local Tkinter GUI with a web-ready Streamlit app.
- [x] Added clean package structure under `src/`.
- [x] Added tests for core model logic.
- [x] Added CI workflow for linting and tests.
- [x] Added Dockerfile for reproducible deployment.
- [x] Replaced personal-style sample data with minimal model-ready data.
- [x] Updated README for recruiters and technical reviewers.

## License

MIT License.