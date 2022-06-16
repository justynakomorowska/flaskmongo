#!/bin/bash
source venv/bin/activate

sleep 20

while true; do
    #flask deploy
    echo "skipping"
    echo $FLASK_APP
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Deploy command failed, retrying in 5 secs...
    sleep 5
done

exec gunicorn -b :5000 --access-logfile - --error-logfile - --certfile=localhost.crt --keyfile=localhost.key app:app
