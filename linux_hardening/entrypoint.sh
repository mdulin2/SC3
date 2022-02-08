#!/bin/bash

# Start multiple processes
/http_server.py &
/ftp_server.py &
  
# Wait for any process to exit
wait -n
  
# Exit with status of process that exited first
exit $?
