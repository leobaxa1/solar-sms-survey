from storage import get_user_data, save_user_data, questions

def handle_incoming_sms(phone, message):
    user_data = get_user_data(phone)
    step = user_data.get('step', 0)

    if step < len(questions):
        user_data[f'Q{step + 1}'] = message.strip()
        step += 1
        user_data['step'] = step
        save_user_data(phone, user_data)

        if step < len(questions):
            return questions[step]
        else:
            return "✅ Thanks! Now please confirm:\nName:\nPhone:\nEmail:\nAddress:"
    elif step == len(questions):
        details = message.strip().split("\n")
        keys = ['Name', 'Phone', 'Email', 'Address']
        for k, v in zip(keys, details):
            user_data[k] = v.strip()
        user_data['step'] += 1
        save_user_data(phone, user_data)
        return "🎉 All set! Thanks for completing the survey."
    else:
        return "You've already completed the survey. Thanks!"

questions = [
    "1. Are you interested in getting Solar Quotation?",
    "2. Do you have existing Solar Panels? Yes/NO",
    "3. What is your Utility Provider for Electricity?",
    "4. What is your Average Electricity Alone?",
    "5. Is your Home Type a Single-Family?",
    "6. Do you have Home Owner's Association?",
]