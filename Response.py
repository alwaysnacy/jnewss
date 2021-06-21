from datetime import datetime


def sample_response(userInput):
    user_mess = str(userInput).lower()

    if user_mess in ('hi', 'hello', 'ok'):
        return 'Hi Bro :D'
    if user_mess in ("time", "time?"):
        now = "Today is " + datetime.now().strftime("%d-%m-%y, %H:%M:%S")
        return str(now)

    return "Sorry We don't understand question :<"
