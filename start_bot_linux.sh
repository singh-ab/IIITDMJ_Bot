#!/bin/bash

while true; do
    read -p "Press Enter to run the code again, or 'q' to quit: " input
    if [ "$input" == "q" ]; then
        break
    fi
    python voiceMail.py
done
