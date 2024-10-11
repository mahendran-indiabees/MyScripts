To expose the metrics from the Robusta KRR CLI tool on port 9090 for Prometheus to scrape, we can modify the existing script in the Robusta KRR GitHub repository. Below are the steps to achieve this, including the necessary Python code and configuration for Prometheus and Grafana.
## Step 1: Modify the Robusta KRR Script
Install Required Python Modules: Ensure you have the necessary Python modules installed. You will need Flask for creating a simple web server and prometheus_client for exposing metrics. You can install them using pip:
```
pip install Flask prometheus_client
```

## Modify the KRR Script: Open the krr.py file in the repository and add the following code to expose metrics on port 9090. Here’s an example of how you can modify the script:
```
from flask import Flask
from prometheus_client import start_http_server, Summary, Gauge
import time
import json
import subprocess

app = Flask(__name__)

# Define Prometheus metrics
cpu_request_gauge = Gauge('krr_cpu_request', 'CPU request for pods', ['pod', 'namespace'])
memory_request_gauge = Gauge('krr_memory_request', 'Memory request for pods', ['pod', 'namespace'])

def collect_krr_metrics():
    # Run the KRR command and capture the output
    result = subprocess.run(['krr', '--output', 'json'], capture_output=True, text=True)
    data = json.loads(result.stdout)

    # Clear previous metrics
    cpu_request_gauge.clear()
    memory_request_gauge.clear()

    # Populate metrics
    for recommendation in data['recommendations']:
        pod = recommendation['pod']
        namespace = recommendation['namespace']
        cpu_request = float(recommendation['cpu_request'].replace('m', '')) / 1000  # Convert to cores
        memory_request = float(recommendation['memory_request'].replace('Mi', '')) / 1024  # Convert to GiB

        cpu_request_gauge.labels(pod=pod, namespace=namespace).set(cpu_request)
        memory_request_gauge.labels(pod=pod, namespace=namespace).set(memory_request)

@app.route('/metrics')
def metrics():
    collect_krr_metrics()
    return '', 200

if __name__ == '__main__':
    start_http_server(9090)  # Start the Prometheus metrics server
    app.run(host='0.0.0.0', port=5000)  # Start the Flask app

```

