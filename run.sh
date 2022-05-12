#!/usr/bin/env bash

# command to run the solution using a production application server
gunicorn --chdir src --bind 0.0.0.0:7000 service:app