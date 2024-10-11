
# Exposing Robusta KRR Metrics to Prometheus and Visualizing in Grafana

This guide explains how to modify the Robusta KRR tool to expose its metrics in a format that Prometheus can scrape, and how to visualize those metrics in Grafana.

## Step 1: Install Required Python Libraries

Install the `prometheus_client` library to expose metrics:

```bash
pip install prometheus_client
```

## Step 2: Modify Robusta KRR CLI to Expose Metrics

Modify the source code of Robusta KRR (e.g., `krr/recommend.py`) to expose metrics via HTTP using the Prometheus Python client. Below is an example Python script that collects KRR recommendations and exposes them to Prometheus:

```python
import subprocess
import json
from prometheus_client import start_http_server, Gauge

# Define Prometheus gauges for CPU and memory savings
cpu_savings_gauge = Gauge('krr_cpu_savings', 'CPU Savings based on KRR recommendations', ['workload'])
mem_savings_gauge = Gauge('krr_memory_savings', 'Memory Savings based on KRR recommendations', ['workload'])

# Function to get KRR recommendations
def get_krr_results():
    result = subprocess.run(['krr', 'recommend', '-f', 'json'], capture_output=True, text=True)
    return json.loads(result.stdout)

# Function to update Prometheus metrics with KRR data
def update_metrics(krr_data):
    for recommendation in krr_data['recommendations']:
        workload = recommendation['workload']
        cpu_savings = recommendation['savings']['cpu']['percentage']
        mem_savings = recommendation['savings']['memory']['percentage']
        
        # Update Prometheus metrics
        cpu_savings_gauge.labels(workload=workload).set(cpu_savings)
        mem_savings_gauge.labels(workload=workload).set(mem_savings)

if __name__ == "__main__":
    # Start HTTP server to expose metrics on port 9090
    start_http_server(9090)
    print("Serving Prometheus metrics on port 9090...")

    while True:
        krr_results = get_krr_results()
        update_metrics(krr_results)
```

### Explanation:
- **KRR recommendations** are collected by invoking the command `krr recommend -f json`.
- **Prometheus metrics** for CPU and memory savings are exposed via HTTP on port `9090`, which Prometheus can scrape.
- The **Prometheus client library** is used to expose metrics in the format Prometheus understands.

## Step 3: Run the Modified Robusta KRR Tool

After modifying the KRR source code, run the script, and it will start an HTTP server exposing the metrics on `http://<your-server>:9090/metrics`.

## Step 4: Configure Prometheus to Scrape KRR Metrics

Add the following configuration to your `prometheus.yml` file:

```yaml
scrape_configs:
  - job_name: 'krr_metrics'
    static_configs:
      - targets: ['localhost:9090']  # Replace with the server and port where KRR is running
```

## Step 5: Install and Configure Grafana

1. **Install Grafana** (for Ubuntu/Debian systems):

   ```bash
   sudo apt-get install -y grafana
   ```

2. **Add Prometheus Data Source in Grafana**:
   - Go to **Configuration > Data Sources** in the Grafana UI.
   - Click **Add data source**.
   - Select **Prometheus** and enter the Prometheus URL (usually `http://localhost:9090`).

3. **Create a Grafana Dashboard**:
   - In Grafana, go to **Create > Dashboard**.
   - Add a **new panel** and enter a Prometheus query to display the KRR metrics. Example queries:
     - CPU Savings: `krr_cpu_savings`
     - Memory Savings: `krr_memory_savings`
   - Adjust the visualization settings as needed to create graphs or tables for better insights.

## Step 6: Visualize KRR Metrics in Grafana

Once the data source is added, create panels in Grafana to visualize the CPU and memory savings reported by KRR. You can display these as:

- Time-series graphs to show the savings trends over time.
- Bar charts to display savings per workload.

## Summary

1. **Modify Robusta KRR source code** to expose metrics using Prometheus.
2. **Run an HTTP server** on port `9090` to expose these metrics.
3. **Configure Prometheus** to scrape metrics from the KRR tool.
4. **Install Grafana**, configure Prometheus as a data source, and create dashboards to visualize the metrics.
