#!/bin/sh

if [ $# -ne 1 ]; then
    exit 1
fi

if [ ! -d "$1" ]; then
    exit 1
fi

for file in "$1"/*; do
    desc=$(file "$file")
    if echo "$desc" | grep -q "ASCII text"; then
        echo "$file: ${desc#*: }"
    fi
done

