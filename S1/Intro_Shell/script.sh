#!/bin/sh

for arg; do
    if [ -x "$arg" ]; then
        echo "$arg"
    fi
done