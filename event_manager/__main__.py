from event_manager import CONFIG
from event_manager.app import app


def main():
    # in production ```gunicorn -w 4 -b 0.0.0.0:8000 app:app with gunicorn```

    # we can use socketio.run(app, host=CONFIG.app.ip, port=CONFIG.app.port, debug=True) instead of app.run(...)
    # if we want to use socketio

    app.run(host=CONFIG.app.ip, port=CONFIG.app.port, debug=True)


if __name__ == '__main__':
    main()
