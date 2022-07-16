#!/bin/bash

if [ "$1" == "log" ] && [ $# -eq 1 ]; then
  if [[ -e log.txt ]]; then
    cat log.txt
  else
    echo "Log file does not exist! Play a game first!"
  fi

else
  clear
  python3 main.py
fi


