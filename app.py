from flask import Flask, request, jsonify
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms3", methods=["POST"])
def sms_reply():
    incoming_msg = request.form.get("Body")
    from_number = request.form.get("From")

    print(f"Message from {from_number}: {incoming_msg}")

    # Respond
    resp = MessagingResponse()
    resp.message("Thanks! We got your message.")
    return str(resp)

@app.route('/export', methods=['GET'])
def export_excel():
    # Replace this with your actual export logic
    filepath = "path/to/exported_file.xlsx"  # or call your export function
    return jsonify({"status": "done", "file": filepath})

@app.route('/', methods=['GET'])
def home():
    return "Solar SMS Survey API is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
