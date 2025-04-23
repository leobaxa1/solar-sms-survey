responses = {}

def get_user_data(phone):
    return responses.get(phone, {})

def save_user_data(phone, data):
    responses[phone] = data

def get_all_responses():
    return responses