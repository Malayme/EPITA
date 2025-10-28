#!/bin/sh

if [ -z "$1" ]; then
    echo "Please provide a directory."
    exit 1
fi

if [ ! -d "$1" ]; then
    echo "The provided argument is not a directory."
    exit 1
fi

find "$1" -type f -name '*.[a-zA-Z][a-zA-Z]'
