#!/bin/sh

if [ "$#" -eq 0 ]; then
    echo "Please provide at least one parameter"
    exit 1
fi

TRASH_DIR="/Users/yannls/Documents/GitHub/exercices_shell/cp/trash"
mkdir "$TRASH_DIR"

for file in *; do
    if [ -d "$file" ]; then
        continue
    fi

    ext="${file##*.}"

    if [ "${#ext}" -eq 1 ] && ! echo "$@" | grep -q "$ext"; then
        mv "$file" "$TRASH_DIR"
    fi
done


