from flask import Flask, render_template, request, jsonify
import requests

RASA_API_URL = "http://localhost:5005/webhooks/rest/webhook"  # Replace with your actual URL

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    user_message = request.json['message']
    print("User Message:", user_message)

    # send user message to Rasa and get bot's response
    rasa_response = requests.post(RASA_API_URL, json={'message': user_message})
    rasa_response_json = rasa_response.json()
    print("Rasa Response:", rasa_response_json)

    bot_response = rasa_response_json[0]['text'] if rasa_response_json else 'Sorry, I didn\'t understand that.'

    return jsonify({'response': bot_response})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, port=3000)