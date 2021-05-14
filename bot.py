from pyrogram import Client, filters, idle
import os.path


def create_application():
    """Initialize app"""
    session_string = load_session_string()
    app = Client(session_string if session_string != '' else ':memory:',
                 config_file="credentials/config.ini")
    return app


def load_session_string():
    """Load saved earlier session
    string from storage file
    Session string - string containing
    info about session"""
    session_string = ''

    if not os.path.exists('credentials/session.txt'):
        return session_string

    with open('credentials/session.txt') as f:
        session_string = f.readline()

    return session_string.strip()


def save_session_string():
    """Save session string to storage file"""
    with open('credentials/session.txt', 'w') as f:
        f.write(app.export_session_string())


app = create_application()

loaded_messages = []
messages_limit = 10


@app.on_message(filters.me)
def download_chat_messages(_, msg):
    """Download chat messages to loaded messages list"""
    msg.delete(revoke=True)
    target = msg.chat.id

    for message in app.iter_history(target, limit=messages_limit):
        loaded_messages.append(message.text)

    save_session_string()


def idle_app():
    """Idle app before chat is selected"""
    idle()


if __name__ == "__main__":
    app.start()
    idle()
    # while True:
    #     print('Next code')
    #     time.sleep(2)
    print(loaded_messages)
    app.stop()
