#!/bin/bash
HOST=localhost
PORT=8080

HOST_PORT="${HOST}:${PORT}"

echo Django is running at ${HOST_PORT}

exec ./manage.py runserver ${HOST_PORT}
