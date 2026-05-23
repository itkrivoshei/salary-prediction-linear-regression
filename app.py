from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from salary_prediction.model import (
    FEATURE_COLUMN,
    TARGET_COLUMN,
    DatasetValidationError,
    PredictionResult,
    load_dataset,
    predict_salary,
    train_regression_model,
)

PROJECT_ROOT = Path(__file__).parent
DEFAULT_DATASET = PROJECT_ROOT / "data" / "salary_data.csv"
MIN_EXPERIENCE_YEARS = 0.0
MAX_EXPERIENCE_YEARS = 40.0
DEFAULT_EXPERIENCE_YEARS = 5.0
EXPERIENCE_STEP = 0.5
ACTUAL_COLOR = "#334155"
PREDICTED_COLOR = "#0f766e"


st.set_page_config(
    page_title="Salary Prediction",
    page_icon="💼",
    layout="centered",
)


@st.cache_data
def load_default_data() -> pd.DataFrame:
    return load_dataset(DEFAULT_DATASET)


def format_salary(value: float) -> str:
    return f"{value:,.0f}"


def format_model_equation(result: PredictionResult) -> str:
    coefficient = float(result.model.coef_[0])
    intercept = float(result.model.intercept_)
    return f"salary = {coefficient:,.2f} × experience_years + {intercept:,.2f}"


def plot_predictions(result: PredictionResult) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(
        result.x_test,
        result.y_test,
        color=ACTUAL_COLOR,
        label="Actual salary",
        alpha=0.85,
    )
    ax.scatter(
        result.x_test,
        result.y_pred,
        color=PREDICTED_COLOR,
        label="Predicted salary",
        alpha=0.9,
    )

    sorted_values = result.x_test.assign(predicted_salary=result.y_pred).sort_values(
        FEATURE_COLUMN
    )
    ax.plot(
        sorted_values[FEATURE_COLUMN],
        sorted_values["predicted_salary"],
        color=PREDICTED_COLOR,
        linewidth=2,
        label="Regression line",
    )

    ax.set_title("Experience vs salary")
    ax.set_xlabel("Experience in years")
    ax.set_ylabel("Salary")
    ax.grid(True, alpha=0.2)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.legend(frameon=False)
    fig.tight_layout()
    return fig


def show_model_metrics(result: PredictionResult) -> None:
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("MSE", f"{result.mse:,.2f}")
    col2.metric("RMSE", f"{result.rmse:,.2f}")
    col3.metric("MAE", f"{result.mae:,.2f}")
    col4.metric("R²", f"{result.r2:.3f}")


def show_model_equation(result: PredictionResult) -> None:
    with st.container(border=True):
        st.markdown("**Fitted model equation**")
        st.code(format_model_equation(result), language="text")
        st.caption("Calculated from the currently loaded dataset.")


def main() -> None:
    st.title("Salary Prediction with Linear Regression")
    st.caption("Single-feature regression demo using years of experience.")
    st.write(
        "Train a simple linear regression model and estimate salary from years of "
        "professional experience."
    )

    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

    try:
        dataset = load_dataset(uploaded_file) if uploaded_file else load_default_data()
    except DatasetValidationError as exc:
        st.error(str(exc))
        st.stop()

    st.subheader("Dataset")
    st.caption(
        f"{len(dataset)} valid rows · feature: `{FEATURE_COLUMN}` · "
        f"target: `{TARGET_COLUMN}`"
    )
    st.dataframe(dataset, use_container_width=True)

    result = train_regression_model(dataset)

    st.subheader("Model metrics")
    show_model_metrics(result)
    show_model_equation(result)

    st.subheader("Prediction chart")
    st.pyplot(plot_predictions(result), clear_figure=True)

    st.subheader("Try a custom prediction")
    experience = st.slider(
        "Experience in years",
        min_value=MIN_EXPERIENCE_YEARS,
        max_value=MAX_EXPERIENCE_YEARS,
        value=DEFAULT_EXPERIENCE_YEARS,
        step=EXPERIENCE_STEP,
    )
    predicted_salary = predict_salary(result.model, experience)
    st.metric("Estimated salary", format_salary(predicted_salary))
    st.caption("Estimate uses only one feature and is not a real salary benchmark.")

    with st.expander("Expected CSV format"):
        st.code("experience_years,salary\n1,42000\n3,56000", language="text")


if __name__ == "__main__":
    main()
