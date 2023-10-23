import os

from event_manager import CONFIG
from event_manager.app import app, socketio


def main():
    socketio.run(app, host=CONFIG.app.ip, port=CONFIG.app.port, allow_unsafe_werkzeug=True)


if __name__ == '__main__':
    main()
