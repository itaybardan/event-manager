# Event Manager

# Installation

```bash
pipenv install
```

#### Configuration file is (here)[event_manager/resources/config.json]

## Setup & Running

1. flask server

```bash
python -m event_manager
```

2. smtp *fake* server (in real life we would want to start a real smtp server on a different service)

```bash
python -m smtpd -n -c DebuggingServer localhost:2500
```

## Example API Usage
#### Few notes:
1. date format should be string yyyy-mm-dd
2. event object is composed of: title, date, location, popularity so the data in the request should be json like the following
```json
{
    "title": "Convention-1",
    "date": "2023-10-23",
    "location": "Tel Aviv",
    "popularity": 100
}
```


```bash
GET: http://localhost:8000/events -> get all events
GET: http://localhost:8000/events?id=1 -> get event with id 1
POST: http://localhost:8000/events -> create new event
PUT: http://localhost:8000/events?id=1 -> update event with id 1
DELETE: http://localhost:8000/events?id=1 -> delete event with id 1
GET: http://localhost:8000/sort_by/creation_time -> get all events sorted by creation time
GET: http://localhost:8000/sort_by/date -> get all events sorted by date
GET: http://localhost:8000/sort_by/popularity -> get all events sorted by popularity
POST: http://localhost:8000/subscribe , data={"event_id": 1, "email": "exmaple@gmail.com"} -> subscribe to event with id 1
POST: http://localhost:8000/bulk_events, data=[event1,event2, event3] -> create multiple events
DELETE: http://localhost:8000/bulk_events, data=[1,2,3,4] -> delete multiple events with ids 1,2,3,4
```

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
        "title": "Convention-3"
    },
    {
        "date": "Mon, 23 Oct 2023 00:00:00 GMT",
        "id": 4,
        "location": "Tel Aviv",
        "popularity": 100,
        "title": "Convention-2"
    },
    {
        "date": "Mon, 23 Oct 2023 00:00:00 GMT",
        "id": 3,
        "location": "Tel Aviv",
        "popularity": 100,
        "title": "Convention-4"
    },
    {
        "date": "Mon, 23 Oct 2023 00:00:00 GMT",
        "id": 2,
        "location": "Tel Aviv",
        "popularity": 100,
        "title": "Convention-1"
    }
]
```

## Current Architecture

this is a simple flask app with a local memory data structure, local fake smtp server, simple rate limiting, simple
scheduler and local db file.

## Optimizations

I didn't have time to optimize the code, but here are some ideas:

1. Add more logging
2. Add load balancing and more flask nodes
3. Add authentication and authorization
4. Make rate limiting more specific (per user, per ip, per event, etc.)
5. Use message queue and workers to send emails instead of the simple scheduler
6. Use a real smtp server
7. Change the local memory data structures to a real databases
8. Add more tests
9. Split to microservices architecture