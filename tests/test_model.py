import pandas as pd
import pytest

from salary_prediction.model import (
    DatasetValidationError,
    predict_salary,
    train_regression_model,
    validate_dataset,
)


def sample_data() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "experience_years": [1, 2, 3, 4, 5, 6, 7, 8],
            "salary": [41000, 48000, 55000, 62000, 69000, 76000, 83000, 90000],
        }
    )


def test_validate_dataset_keeps_required_columns() -> None:
    data = sample_data().assign(extra_column="ignored")

    result = validate_dataset(data)

    assert list(result.columns) == ["experience_years", "salary"]
    assert len(result) == 8


def test_validate_dataset_rejects_missing_columns() -> None:
    data = pd.DataFrame({"experience_years": [1, 2, 3]})

    with pytest.raises(DatasetValidationError, match="Missing required column"):
        validate_dataset(data)


def test_validate_dataset_rejects_too_few_valid_rows() -> None:
    data = pd.DataFrame(
        {
            "experience_years": [1, 2, None, None, None],
            "salary": [41000, 48000, None, None, None],
        }
    )

    with pytest.raises(DatasetValidationError, match="at least five valid rows"):
        validate_dataset(data)


def test_validate_dataset_rejects_negative_experience() -> None:
    data = sample_data()
    data.loc[0, "experience_years"] = -1

    with pytest.raises(DatasetValidationError, match="cannot be negative"):
        validate_dataset(data)


def test_validate_dataset_rejects_non_positive_salary() -> None:
    data = sample_data()
    data.loc[0, "salary"] = 0

    with pytest.raises(DatasetValidationError, match="greater than zero"):
        validate_dataset(data)


def test_train_regression_model_returns_metrics() -> None:
    result = train_regression_model(sample_data())

    assert result.mse >= 0
    assert result.rmse >= 0
    assert result.mae >= 0
    assert result.r2 <= 1


def test_predict_salary_returns_positive_number() -> None:
    result = train_regression_model(sample_data())

    prediction = predict_salary(result.model, 10)

    assert prediction > 0


def test_predict_salary_rejects_negative_experience() -> None:
    result = train_regression_model(sample_data())

    with pytest.raises(ValueError, match="cannot be negative"):
        predict_salary(result.model, -1)
