# event-manager


# Installation
```bash
pipenv install
```

#### Configuration file is (here)[event_manager/resources/config.json]


# Setup & Running
1. flask server
```bash
python -m event_manager
```
2. smtp *fake* server (in real life we would want to start a real smtp server on a different service)
```bash
python -m smtpd -n -c DebuggingServer localhost:2500
```



## Example API Usage
```bash
GET: http://localhost:8000/events -> get all events
GET: http://localhost:8000/events?id=1 -> get event with id 1
POST: http://localhost:8000/events -> create new event
PUT: http://localhost:8000/events?id=1 -> update event with id 1
DELETE: http://localhost:8000/events?id=1 -> delete event with id 1
```

## Example Output
```GET: http://localhost:port/sort_by/creation_time```
```json
[
    {
        "date": "Fri, 27 Oct 2023 00:00:00 GMT",
        "id": 5,
        "location": "Bat Yam",
        "popularity": 1000,
        "title": "wedding"
    },
    {
        "date": "Mon, 23 Oct 2023 00:00:00 GMT",
        "id": 4,
        "location": "Tel Aviv",
        "popularity": 100,
        "title": "Derby"
    },
    {
        "date": "Mon, 23 Oct 2023 00:00:00 GMT",
        "id": 3,
        "location": "Tel Aviv",
        "popularity": 100,
        "title": "Derby"
    },
    {
        "date": "Mon, 23 Oct 2023 00:00:00 GMT",
        "id": 2,
        "location": "Tel Aviv",
        "popularity": 100,
        "title": "Derby"
    }
]
```
