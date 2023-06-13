from flask import Flask, jsonify, request

app = Flask(__name__)

# Define a route to handle API requests from the frontend
@app.route('/api/data', methods=['GET'])
def get_data():
    # Process the request and return data
    # You can fetch data from a database or perform any required operations here
    data = {'message': 'Hello from the backend!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run()
