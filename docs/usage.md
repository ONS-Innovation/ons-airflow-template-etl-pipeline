# How to Test and Run This Project

## 1. Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## 2. Set Up Pre-commit Hooks

```bash
pre-commit install
```

## 3. Linting and Security Checks

```bash
make lint
make security
```

## 4. Run Unit and End-to-End Tests

```bash
make test
make
```

## 5. Run Airflow and the ETL DAG

### a. Copy Your DAG to Airflow's DAGs Folder

```bash
mkdir -p ~/airflow/dags
cp dags/etl_workflow.py ~/airflow/dags/
```

### b. Start Airflow

```bash
airflow standalone
```

- The Airflow UI will be available at [http://localhost:8080](http://localhost:8080).
- Log in with the credentials shown in your terminal or in `~/airflow/simple_auth_manager_passwords.json.generated`.

### c. Trigger the DAG

- In the Airflow UI, find `etl_workflow`.
- Toggle it "On" and click the "Play" button to trigger a run.
- Click on each task to view logs and confirm successful execution.

## 6. (Optional) Run the ETL Script Manually

```bash
python scripts/run_etl.py
```

---

**Note:**
- If you change your ETL code, restart Airflow to reload the DAG.
- For troubleshooting, check the Airflow UI for import errors or task logs.

## Usage

The ETL pipeline consists of three main components:

- **Extract**: The `extract_data` function retrieves data from the source.
- **Transform**: The `transform_data` function processes the extracted data.
- **Load**: The `load_data` function loads the transformed data into the target destination.

The Airflow DAG defined in `dags/etl_workflow.py` orchestrates these tasks, ensuring they run in the correct order.
