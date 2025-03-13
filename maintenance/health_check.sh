#!/bin/bash
if pgrep -x "node" > /dev/null
then
    echo "App is running"
else
    echo "App is down!"
fi
