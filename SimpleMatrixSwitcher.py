from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')
	
@app.route('/forward_request', methods=['POST'])
def forward_request():
	try:
		data = request.data
		print(data.decode('UTF-8'))
		ip_address = "matrixIp/video.set"		
		response = requests.post('http://'+ip_address, data=data.decode('UTF-8'))
		return 'Success'
	except Exception as e:
		return jsonify({"error": str(e)}), 500
		
if __name__ == '__main__':
	app.run(debug=True)
