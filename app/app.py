from flask import Flask
from prometheus_client import start_http_server, Summary
import random
import time

app = Flask(__name__)

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@app.route('/')
@REQUEST_TIME.time()
def hello():
    time.sleep(random.random())
    return "Hello, Prometheus!"

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)  # Exposes metrics at http://localhost:8000
    app.run(host='0.0.0.0', port=5000)
