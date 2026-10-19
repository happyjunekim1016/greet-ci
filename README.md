# greet-ci

A one-file greeting program with a GitHub Actions CI workflow.

## Install

```bash
uv sync --locked
```

## Run

```bash
uv run --locked python greet.py Hee   # Hello, Hee!
uv run --locked python greet.py       # Hello, world!
```

## Check

```bash
uv run --locked pytest -q greet.py
uv run --locked black --check greet.py
uv run --locked flake8 greet.py
uv run --locked mypy greet.py
uv build
```
