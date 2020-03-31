from flask import Flask, request, render_template
from twilio.rest import Client
import config

app = Flask(__name__)

@app.route("/")
def home():
  return render_template('home.html')

@app.route('/send_sms', methods=['POST'])
def send_sms():
  if request.method == 'POST':
    # Store form data
    phone_number = request.form['phone']
    message = request.form['message']
    # Create account credentials for api
    account_sid = config.ACCOUNT_SID
    auth_token = config.AUTH_TOKEN
    # Create connection to twilio and send message
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                      body= f"{message}",
                      from_="+19153171361",
                      to= f"+1{phone_number}"
                    )

    return render_template('message_sent.html')
  return home()

if __name__ == "__main__": 
  app.run(debug=True)
