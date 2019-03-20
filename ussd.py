from flask import Flask, request

app = Flask(__name__)

response = " "

""" A simple USSD menu that asks users to enter 1 to view their account 
and 2 to view their phone number. On the accounts page, 
they can enter 1 for the account number or 2 for the account balance. """

@app.route('/ussd', methods=['POST', 'GET'])
def ussd_callback():
	#define parameters receives from AT's API
	global response
	session_id = request.values.get("sessionId", None)
	service_code = request.values.get("serviceCode", None)
	phone_number = request.values.get("phoneNumber", None)
	text = request.values.get("text", "default")

	# When 'text' variable is empty, it means we are starting the session
	# hence we display the initial page.
	# NB: The plaintext o/p starts with:
	# 	END - to put an end to a session
	# 	CON - to continue it 

	if text == ' ':
		response = "CON What would you want to check? \n"
		response += "1. My Account \n"
		response += "2. My phone number "

	#""" when text = 1, show the account page """
	elif text == '1':
		response = "CON Choose account info you want to view \n"
		response += "1. Account number \n"
		response += "2. Account balance "

	#""" text = 1*1, show account number page """
	elif text == '1*1':	
		accountNumber = "SPH/0001/019"
		response = "END Your account number is " + accountNumber

	#""" text = 1*2, show account balance page """
	elif text == '1*2':	
		balance = "KES 2,200"
		response = "END Your balance is " + balance

	#""" text = 2, show phone number page """
	elif text == '2':
		response = "This is your phone number: " + phone_number

	return response

if __name__ == "__main__":
	app.run()

