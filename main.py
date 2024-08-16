# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route('/')
# def home():
#     return "Hello, World!"
#
# @app.route('/hello')
# def hello():
#     return "Hello from another route!"
#
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=81)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/hello')
def hello():
    return "Hello from another route!"

@app.route('/health')
def health():
    # This endpoint is for Kubernetes liveness probe
    return "Healthy", 200

@app.route('/readiness')
def readiness():
    # This endpoint is for Kubernetes readiness probe
    return "Ready", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)  # Change the port to 80
