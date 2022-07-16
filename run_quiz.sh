clear

if [[ "$1" == "log" ]]; then
  if [[ -e log.txt ]]; then
    cat log.txt
  else
    echo "Log file does not exist! Play a game first!"
  fi

else
  python3 main.py
fi


