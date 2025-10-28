#!/bin/sh

for i in $(seq 10); do
    if [ "$i" -lt 5 ]; then
        continue
    fi
    echo "$i"
done