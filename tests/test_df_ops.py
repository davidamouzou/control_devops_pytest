import pandas as pd
import pytest

from src.df_ops import (
    build_dataframe,
    filter_by_department,
    mean_age,
    mean_salary,
    row_count,
)


def test_build_dataframe_structure() -> None:
    df = build_dataframe()
    assert list(df.columns) == ["age", "salaire", "departement"]
    assert len(df) == 8
    assert pd.api.types.is_integer_dtype(df["age"])
    assert pd.api.types.is_float_dtype(df["salaire"])
    assert pd.api.types.is_object_dtype(df["departement"])


def test_means() -> None:
    df = build_dataframe()
    assert mean_age(df) == pytest.approx(34.5)
    assert mean_salary(df) == pytest.approx(3775.0)


def test_filter_by_department_it() -> None:
    df = build_dataframe()
    filtered = filter_by_department(df, "IT")
    assert (filtered["departement"] == "IT").all()
    assert len(filtered) == 4


def test_row_count() -> None:
    df = build_dataframe()
    assert row_count(df) == 8
