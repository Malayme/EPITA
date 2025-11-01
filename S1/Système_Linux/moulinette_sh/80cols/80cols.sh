#!/bin/sh

if [ "$#" -ne 1 ] || [ ! -r "$1" ]; then
    exit 1
fi

while IFS= read -r line; do
    case "$line" in
        *\\n*)
            ;;
    esac
    l=$(echo -n "$line" | wc -c)
    if [ "$l" -ge 80 ]; then
        printf "%s\n" "$line"
    fi
done < "$1"

exit 0
