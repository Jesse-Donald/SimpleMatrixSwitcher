from flask import Flask, request, jsonify, render_template
import requests
import os
import json

app = Flask(__name__)
MATRIX_IP = os.environ.get("MATRIX_IP", "192.168.1.100")
CONTAINER_ADDRESS = os.environ.get("CONTAINER_ADDRESS", "http://localhost:8000")
raw_items = os.environ.get("SOURCE_LABELS", "[]")
try:
    items = json.loads(raw_items)
except json.JSONDecodeError:
    items = []

@app.route('/')
def index():
	return render_template('index.html', matrixip=MATRIX_IP, container=CONTAINER_ADDRESS, source_labels=items)
	
@app.route('/forward_request', methods=['POST'])
def forward_request():
	try:
		data = request.data
		print(data.decode('UTF-8'))
		ip_address = MATRIX_IP + "/video.set"		
		response = requests.post('http://'+ip_address, data=data.decode('UTF-8'))
		return 'Success'
	except Exception as e:
		return jsonify({"error": str(e)}), 500
		
if __name__ == '__main__':
	app.run(debug=True)
