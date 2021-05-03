from datetime import datetime


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi"):
        return "Yoroshiku!"

    if  user_message in ("nani"):
        return "Oi ningen!"

    if user_message in ("time"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "Wakarimasen! :'("