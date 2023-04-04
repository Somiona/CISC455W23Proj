#!/bin/zsh

deno task --cwd ./frontend -c ./frontend/deno.json start &
deno_pid=$!
pipenv run flask --app ./backend/index run &
flask_pid=$!

trap "kill $deno_pid $flask_pid" SIGINT SIGTERM EXIT

wait