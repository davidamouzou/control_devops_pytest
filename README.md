# Controle DevOps - Pytest et GitHub Actions

Petit projet Python pour manipuler un DataFrame pandas et valider les fonctions
avec pytest. Les tests sont executes automatiquement via GitHub Actions.

Auteur: AMOUZOU David

## Structure

- `src/df_ops.py` : fonctions de manipulation du DataFrame
- `tests/test_df_ops.py` : tests pytest
- `requirements.txt` : dependances
- `.github/workflows/ci.yml` : pipeline CI

## Prerequis

- Python 3.10+

## Installation

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## Tests

```bash
pytest
```

## Mesurez la couverture de vos tests avec pytest-cov

```bash
pytest --cov=src tests/
```