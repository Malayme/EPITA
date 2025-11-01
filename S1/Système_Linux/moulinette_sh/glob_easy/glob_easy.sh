#!/bin/sh

dir="$1"
result=""

for file in "$dir"/*.[a-zA-Z][a-zA-Z]; do
    if [ -f "$file" ]; then
        result="$result $file"        
    fi
done

echo ${result}



