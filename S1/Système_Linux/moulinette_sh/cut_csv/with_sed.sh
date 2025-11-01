#!/bin/sh

#commentaire de modification
if [ "$#" -ne 2 ]; then
  exit 1
fi

file="$1"
line_number="$2"

if [ ! -f "$file" ]; then
  exit 1
fi

case "$line_number" in
  ''|*[!0-9]*)
    exit 1
    ;;
esac

line=$(sed -n "${line_number}p" "$file")

if [ -z "$line" ]; then
  exit 1
fi

column2=$(echo "$line" | sed 's/^[^;]*;\([^;]*\);.*$/\1/')
column3=$(echo "$line" | sed 's/^[^;]*;[^;]*;\([^;]*\);.*$/\1/')

echo "$column2 is $column3"

exit 0
