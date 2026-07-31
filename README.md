# SQL SRS — Spaced-Repetition SQL Trainer

A small [Streamlit](https://streamlit.io/) app to practice SQL queries and keep them sharp
over time, backed by an in-process [DuckDB](https://duckdb.org/) database. Pick a theme,
write your query, and the app checks your result against the expected solution.

## Features

- **Practice by theme** — `cross_joins`, `Groupby`, `window_functions`.
- **Instant feedback** — runs your SQL against DuckDB and `compare()`s your result to the
  reference solution (column mismatches and row-count differences are reported).
- **Spaced repetition** — a `memory_state` table tracks each exercise's `last_reviewed`
  date, so exercises are surfaced oldest-first for review.
- **Self-contained** — the database and exercise tables are built on first run by
  `init_db.py`; reference answers live in `answers/*.sql`.
- **CI** — a GitHub Actions workflow enforces `black` formatting on every pull request.

## Tech stack

Python · Streamlit · DuckDB · pandas · GitHub Actions (Black)

## Getting started

```bash
pip install -r requirements.txt
streamlit run app.py
```

On first launch the app creates `data/exercices_sql_tables.duckdb` (via `init_db.py`) and
opens in your browser. Select a theme in the sidebar, type your query, and compare it to the
solution.

## Project structure

```
app.py            # Streamlit app: query input, result comparison, tables/solution tabs
init_db.py        # builds the DuckDB database, exercise tables and memory_state
answers/          # reference SQL solutions, one file per exercise
requirements.txt
.github/workflows/check_code_quality.yaml  # Black formatting check on PRs
```
