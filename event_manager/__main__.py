from event_manager import CONFIG
from event_manager.app import app, socketio


# socketio.run(app, host=CONFIG.app.ip, port=CONFIG.app.port, allow_unsafe_werkzeug=True, debug=True)


def main():
    # in production ```gunicorn -w 4 -b 0.0.0.0:8000 app:app with gunicorn```
    socketio.run(app, host=CONFIG.app.ip, port=CONFIG.app.port, allow_unsafe_werkzeug=True, debug=True)


if __name__ == '__main__':
    main()
