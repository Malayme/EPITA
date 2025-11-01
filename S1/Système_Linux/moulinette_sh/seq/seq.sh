#!/bin/sh

FIRST=$1
INCREMENT=$2
LAST=$3

if [ "$#" -ne 3 ]; then
    echo "Usage: ./seq.sh FIRST INCREMENT LAST" >&2
    exit 1
fi

if ! [ "$INCREMENT" -ne 0 ] 2>/dev/null; then
    exit 1
fi

if [ "$FIRST" -eq "$LAST" ]; then
    echo "$FIRST"
    exit 0
fi

if [ "$FIRST" -lt "$LAST" ]; then
    if [ "$INCREMENT" -le 0 ]; then
        exit 1
    fi
    n="$FIRST"
    while [ "$n" -le "$LAST" ]; do
        echo "$n"
        n=$((n + INCREMENT))
    done
    exit 0
fi

if [ "$FIRST" -gt "$LAST" ]; then
    if [ "$INCREMENT" -ge 0 ]; then
        exit 1
    fi
    n="$FIRST"
    while [ "$n" -ge "$LAST" ]; do
        echo "$n"
        n=$((n + INCREMENT))
    done
    exit 0
fi
