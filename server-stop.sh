#!/bin/bash

pid="$(pgrep -f 5000)"
if [ ${#pid} -ge 1 ]; then
  kill ${pid}
  echo "Sero killed"
else
  echo "Sero is not running"
fi
