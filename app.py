from flask import Flask, request, jsonify
from survey_logic import handle_incoming_sms
import export

app = Flask(__name__)

@app.route('/sms-webhook', methods=['POST'])
def sms_webhook():
    incoming = request.get_json()
    phone = incoming.get('phone')
    message = incoming.get('message')

    response = handle_incoming_sms(phone, message)
    return jsonify({"status": "ok", "message": response})

@app.route('/export', methods=['GET'])
def home():
    return "Solar SMS Survey API is running!"
def export_excel():
    filepath = export.export_to_excel()
    return jsonify({"status": "done", "file": filepath})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Bind to 0.0.0.0 for Render
