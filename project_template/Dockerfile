FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements files
COPY requirements.txt requirements-dev.txt ./

# Install production dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install development dependencies
RUN pip install --no-cache-dir -r requirements-dev.txt

# Copy the entire project
COPY . .

# Expose the necessary port for Airflow (if needed)
EXPOSE 8080

# Command to run the ETL process
CMD ["python", "scripts/run_etl.py"]
