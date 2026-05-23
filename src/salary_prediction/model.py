from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import BinaryIO

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

FEATURE_COLUMN = "experience_years"
TARGET_COLUMN = "salary"
REQUIRED_COLUMNS = {FEATURE_COLUMN, TARGET_COLUMN}


class DatasetValidationError(ValueError):
    """Raised when the input dataset cannot be used for model training."""


@dataclass(frozen=True)
class PredictionResult:
    model: LinearRegression
    x_test: pd.DataFrame
    y_test: pd.Series
    y_pred: pd.Series
    mse: float
    rmse: float
    mae: float
    r2: float


def load_dataset(source: str | Path | BinaryIO) -> pd.DataFrame:
    data = pd.read_csv(source)
    return validate_dataset(data)


def validate_dataset(data: pd.DataFrame) -> pd.DataFrame:
    missing_columns = REQUIRED_COLUMNS.difference(data.columns)
    if missing_columns:
        missing = ", ".join(sorted(missing_columns))
        raise DatasetValidationError(f"Missing required column(s): {missing}")

    cleaned = data[[FEATURE_COLUMN, TARGET_COLUMN]].copy()
    cleaned[FEATURE_COLUMN] = pd.to_numeric(cleaned[FEATURE_COLUMN], errors="coerce")
    cleaned[TARGET_COLUMN] = pd.to_numeric(cleaned[TARGET_COLUMN], errors="coerce")
    cleaned = cleaned.dropna()

    if len(cleaned) < 5:
        raise DatasetValidationError("Dataset must contain at least five valid rows.")

    if (cleaned[FEATURE_COLUMN] < 0).any():
        raise DatasetValidationError("Experience values cannot be negative.")

    if (cleaned[TARGET_COLUMN] <= 0).any():
        raise DatasetValidationError("Salary values must be greater than zero.")

    return cleaned.reset_index(drop=True)


def train_regression_model(data: pd.DataFrame) -> PredictionResult:
    cleaned = validate_dataset(data)
    x = cleaned[[FEATURE_COLUMN]]
    y = cleaned[TARGET_COLUMN]

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.2,
        random_state=42,
    )

    model = LinearRegression()
    model.fit(x_train, y_train)
    y_pred = model.predict(x_test)

    mse = mean_squared_error(y_test, y_pred)
    rmse = mse**0.5
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    return PredictionResult(
        model=model,
        x_test=x_test,
        y_test=y_test,
        y_pred=pd.Series(y_pred, index=y_test.index),
        mse=mse,
        rmse=rmse,
        mae=mae,
        r2=r2,
    )


def predict_salary(model: LinearRegression, experience_years: float) -> float:
    if experience_years < 0:
        raise ValueError("Experience cannot be negative.")

    prediction_input = pd.DataFrame({FEATURE_COLUMN: [experience_years]})
    return float(model.predict(prediction_input)[0])
