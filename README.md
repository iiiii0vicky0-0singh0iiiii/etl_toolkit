# 🔧 ETL Toolkit

> A modular, production-ready data pipeline framework built in Python — with UI, scheduling, validation, and plugin support.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-ff4b4b?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Airflow](https://img.shields.io/badge/Orchestration-Apache%20Airflow-017CEE?logo=apacheairflow&logoColor=white)](https://airflow.apache.org)
[![Great Expectations](https://img.shields.io/badge/Validation-Great%20Expectations-orange)](https://greatexpectations.io)

---

## 📌 Overview

**ETL Toolkit** is a scalable, configurable ETL framework designed for real-world data engineering workflows. It lets you extract data from multiple sources, apply custom transformations, validate data quality, and load results into your storage systems — all with minimal boilerplate.

Whether you're building ML data prep pipelines, automated reporting workflows, or analytics dashboards, ETL Toolkit gives you the building blocks to do it cleanly and reliably.

---

## ✨ Features

| Category | Capabilities |
|---|---|
| 🔹 **Core ETL** | CSV, API & database extraction; data cleaning & transformation; CSV & database loading |
| 🎨 **UI** | Interactive Streamlit dashboard; visual pipeline runner; dataset upload |
| ⏱️ **Orchestration** | Apache Airflow DAGs; scheduling & retry mechanisms |
| 🧪 **Validation** | Great Expectations data quality checks; schema & constraint validation |
| 📊 **Logging** | Centralized logging; execution tracking & debugging |
| 🧩 **Plugins** | Custom transformation plugins; dynamically loaded user-defined logic |

---

## 🏗️ Project Structure

```
etl_toolkit/
│
├── app.py                  # Main pipeline runner
├── streamlit_app.py        # UI application
├── config.yaml             # Pipeline configuration
├── requirements.txt
│
├── extract/                # Data extraction modules
├── transform/              # Data transformation logic
├── load/                   # Data loading modules
│
├── plugins/                # Custom transformations
├── validation/             # Data validation configs
├── dags/                   # Airflow DAGs
├── logs/                   # Log files
│
└── data/
    ├── raw/
    └── processed/
```

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/etl-toolkit.git
cd etl-toolkit
pip install -r requirements.txt
```

---

## ▶️ Usage

### Run Basic Pipeline

```bash
python app.py
```

### Run with Config

```bash
python app.py --config config.yaml
```

### Launch Streamlit UI

```bash
streamlit run streamlit_app.py
```

---

## ⚙️ Configuration

Define your full pipeline in `config.yaml`:

```yaml
extract:
  type: csv
  path: data/raw/sample.csv

transform:
  drop_duplicates: true
  fillna: ffill

load:
  type: csv
  path: data/processed/output.csv
```

---

## 🧪 Data Validation

Use [Great Expectations](https://greatexpectations.io) to enforce data quality rules:

```python
import great_expectations as ge

df = ge.from_pandas(df)
df.expect_column_values_to_not_be_null("name")
```

Validation configs live in the `validation/` directory and can be extended for custom schema rules and constraints.

---

## 🧩 Plugin System

Drop a custom transformation into the `plugins/` directory:

```python
# plugins/custom_transform.py

def transform(df):
    df["new_column"] = df["value"] * 2
    return df
```

The pipeline dynamically loads and applies any plugins it finds — no changes to core code required.

---

## ⏱️ Airflow Integration

1. Define your DAG in `dags/etl_dag.py`
2. Schedule pipelines (daily, hourly, or custom cron)
3. Monitor execution via the Airflow web UI

```python
# Example DAG snippet
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

with DAG("etl_pipeline", start_date=datetime(2024, 1, 1), schedule_interval="@daily") as dag:
    run_pipeline = PythonOperator(
        task_id="run_etl",
        python_callable=run_etl_pipeline
    )
```

---

## 📊 Logging & Monitoring

All execution logs are written to `logs/etl.log`. The logging system tracks:

- Pipeline start/end timestamps
- Per-step execution flow
- Errors and warnings with tracebacks
- Data row counts pre/post transformation

---

## 🧠 Tech Stack

- **Python** — Core language
- **Pandas** — Data manipulation
- **Streamlit** — Interactive UI
- **Apache Airflow** — Pipeline orchestration
- **Great Expectations** — Data validation
- **SQLAlchemy** — Database abstraction

---

## 🎯 Use Cases

- Data preprocessing pipelines
- Machine learning data preparation
- Automated reporting workflows
- ETL for analytics dashboards

---

## 🚀 Roadmap

- [ ] Data warehouse support (BigQuery, Snowflake)
- [ ] Real-time streaming via Apache Kafka
- [ ] Dockerized deployment
- [ ] UI authentication layer

---

## 🤝 Contributing

Contributions are welcome! To get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m 'Add my feature'`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).


---

⭐ If this project helps you, give it a star on GitHub — it means a lot!
