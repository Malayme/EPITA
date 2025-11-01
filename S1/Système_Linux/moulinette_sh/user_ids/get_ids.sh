#!/bin/sh

cut -d':' -f3 /etc/passwd | sort -rn | while read id1; do
  if [ "$id2" != "$id1" ]; then
    echo "$id1"
    id2="$id1"
  fi
done
