#!/bin/zsh
# Author: Somiona Tian (17ht13@queensu.ca)
# Disclaimer: This script is being tested under Ubuntu 20.10

yarn --cwd ./frontend dev &
yarn_pid=$!
pipenv run flask --app ./backend/index run &
flask_pid=$!

trap "kill $yarn_pid $flask_pid" SIGINT SIGTERM EXIT

wait