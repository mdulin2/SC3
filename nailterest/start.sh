#!/bin/bash

## Start up the backend
tmux new-session -d -s backend 'cd ./application/backend && python3 main.py'

## Start the frontend
tmux new-session -d -s frontend 'cd ./application/frontend && python3 -m http.server 8080'

# Start the flag server
tmux new-session -d -s flag_host 'cd ./flag_host && python3 main.py'


sleep 1000000