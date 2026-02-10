from __future__ import annotations

import pandas as pd


_REQUIRED_COLUMNS = ["age", "salaire", "departement"]


def _validate_columns(df: pd.DataFrame) -> None:
    # Verifie la presence des colonnes attendues.
    missing = [col for col in _REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        raise ValueError(
            f"Le DataFrame doit contenir les colonnes {_REQUIRED_COLUMNS}. "
            f"Colonnes manquantes: {missing}"
        )


def build_dataframe() -> pd.DataFrame:
    # Construit le DataFrame avec les donnees imposees par l'ennonce.
    data = {
        "age": [25, 30, 22, 45, 35, 28, 50, 41],
        "salaire": [2800.0, 3200.0, 2100.0, 5000.0, 3800.0, 2600.0, 6200.0, 4500.0],
        "departement": pd.Series(
            ["IT", "IT", "HR", "Finance", "IT", "HR", "Finance", "IT"], dtype="object"
        ),
    }
    return pd.DataFrame(data)


def mean_age(df: pd.DataFrame) -> float:
    # Calcule la moyenne de la colonne age.
    _validate_columns(df)
    return float(df["age"].mean())


def mean_salary(df: pd.DataFrame) -> float:
    # Calcule la moyenne de la colonne salaire.
    _validate_columns(df)
    return float(df["salaire"].mean())


def filter_by_department(df: pd.DataFrame, dept: str) -> pd.DataFrame:
    # Filtre les lignes selon la valeur de departement.
    _validate_columns(df)
    return df[df["departement"] == dept]


def row_count(df: pd.DataFrame) -> int:
    # Renvoie le nombre total de lignes.
    _validate_columns(df)
    return int(len(df))
