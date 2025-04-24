# storage.py

responses = {}

# Questions list
questions = [
    "Are you interested in getting Solar Quotation?",
    "Do you have existing Solar Panels? Yes/NO",
    "What is your Utility Provider for Electricity?",
    "What is your Average Electricity Alone?",
    "Is your Home Type a Single-Family?",
    "Do you have Home Owner's Association?"
]

def get_user_data(phone):
    return responses.get(phone, {})

def save_user_data(phone, data):
    responses[phone] = data

def get_all_responses():
    return responses
