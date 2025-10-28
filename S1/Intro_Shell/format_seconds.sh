#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <secondes>"
    exit 1
fi

minutes=$(($1 / 60))
secondes=$(($1 % 60))

if [ $secondes -lt 10 ]; then
    secondes="0$secondes"
fi 

echo "$minutes:$secondes"

#transforme les secondes en minutes
