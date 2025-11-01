#!/bin/sh

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

big_line=$(wc -l < "$file")
if [ "$line_number" -gt "$big_line" ]; then
  exit 1
fi

line=$(head -n "$line_number" "$file" | tail -n 1)

if [ -z "$line" ]; then
  exit 1
fi

column2=$(echo "$line" | cut -d';' -f2)
column3=$(echo "$line" | cut -d';' -f3)


echo "$column2 is $column3"

exit 0
