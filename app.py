from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from salary_prediction.model import (
    DatasetValidationError,
    PredictionResult,
    load_dataset,
    predict_salary,
    train_regression_model,
)

PROJECT_ROOT = Path(__file__).parent
DEFAULT_DATASET = PROJECT_ROOT / "data" / "salary_data.csv"


st.set_page_config(
    page_title="Salary Prediction",
    page_icon="💼",
    layout="centered",
)


@st.cache_data
def load_default_data() -> pd.DataFrame:
    return load_dataset(DEFAULT_DATASET)


def plot_predictions(result: PredictionResult) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(result.x_test, result.y_test, label="Actual salary")
    ax.scatter(result.x_test, result.y_pred, label="Predicted salary")

    sorted_values = result.x_test.assign(predicted_salary=result.y_pred).sort_values(
        "experience_years"
    )
    ax.plot(
        sorted_values["experience_years"],
        sorted_values["predicted_salary"],
        linewidth=2,
        label="Regression line",
    )

    ax.set_title("Experience vs salary")
    ax.set_xlabel("Experience in years")
    ax.set_ylabel("Salary")
    ax.grid(True, alpha=0.3)
    ax.legend()
    return fig


def main() -> None:
    st.title("Salary Prediction with Linear Regression")
    st.write(
        "Train a simple linear regression model and estimate salary from years of "
        "professional experience."
    )

    uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

    try:
        data = load_dataset(uploaded_file) if uploaded_file else load_default_data()
    except DatasetValidationError as exc:
        st.error(str(exc))
        st.stop()

    st.subheader("Dataset")
    st.dataframe(data, use_container_width=True)

    result = train_regression_model(data)

    st.subheader("Model metrics")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("MSE", f"{result.mse:,.2f}")
    col2.metric("RMSE", f"{result.rmse:,.2f}")
    col3.metric("MAE", f"{result.mae:,.2f}")
    col4.metric("R²", f"{result.r2:.3f}")

    st.subheader("Prediction chart")
    st.pyplot(plot_predictions(result), clear_figure=True)

    st.subheader("Try a custom prediction")
    experience = st.slider(
        "Experience in years",
        min_value=0.0,
        max_value=40.0,
        value=5.0,
        step=0.5,
    )
    predicted_salary = predict_salary(result.model, experience)
    st.success(f"Estimated salary: {predicted_salary:,.0f}")

    with st.expander("Expected CSV format"):
        st.code("experience_years,salary\n1,42000\n3,56000", language="text")


if __name__ == "__main__":
    main()
