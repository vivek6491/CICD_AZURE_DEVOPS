app = Flask(__name__)
@app.route('/')
def hello():
    return jsonify(message="Hello from Azure DevOps CI/CD")
if __name__ == '__master__':
    app.run(host='0.0.0.0', port=5000)
