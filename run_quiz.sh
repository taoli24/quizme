#!/bin/bash

if [ "$1" == "--log" ] && [ $# -eq 1 ]; then
  if [[ -e log.txt ]]; then
    cat log.txt
  else
    echo "Log file does not exist! Play a game first!"
  fi

elif [ $# -eq 1 ] && [ "$1" == "--help" ]; then
  cat help.txt

elif [ $# -eq 0 ]; then
  clear
  python3 main.py
else
  echo "Unknown parameter, try run ./run_quiz.sh --help"
fi


