#!/bin/sh

while read -r line; do
  res=$(echo "$line" | grep -o '^[[:space:]]*\(.*\)[[:space:]]*$' | grep -o '\S.*\S\|\S')

  if [ -z "$res" ]; then
    echo "it is empty"
  elif echo "$res" | grep -Eq '^[a-zA-Z]+$'; then
    echo "it is a word"
  elif echo "$res" | grep -Eq '^[0-9]$'; then
    echo "it is a digit"
  elif echo "$res" | grep -Eq '^[0-9]{2,}$'; then
    echo "it is a number"
  elif echo "$res" | grep -Eq '^[a-zA-Z0-9]+$'; then
    echo "it is an alphanum"
  else
    echo "it is too complicated"
    exit 0
  fi
done
