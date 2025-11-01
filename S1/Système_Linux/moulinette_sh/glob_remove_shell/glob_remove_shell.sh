#!/bin/sh

EXTENSION=${1:-txt}
FILES=0

for FILE in *.$EXTENSION; do
    if [ -f "$FILE" ]; then
        FILES=$((FILES+1))
        rm "$FILE"
    fi
done


if [ $FILES -eq 0 ]; then
    exit 1
fi

exit 0
