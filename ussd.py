from flask import Flask, request

app = Flask(__name__)

response = ""

@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
	global response
	session_id = request.values.get("sessionId", None)
	service_code = request.values.get("serviceCode", None)
	phone_number = request.values.get("phoneNumber", None)
	text = request.values.get("text", "default")