#!/bin/sh

calcul() {
    expr="$1"

    expr=$(echo "$expr" | while IFS= read -r line; do
        printf "%s" "$line"
    done)

    result=$( (eval "echo \$(( $expr ))" 2>/dev/null) || echo "error" )
    
    if [ "$result" = "error" ]; then
        echo "Invalid expression: $expr" >&2
        return 1
    else
        echo "$result"
    fi
}

if [ $# -gt 0 ]; then
    calcul "$1"
    exit $?
fi

while true; do
    read -r expr
    if [ -z "$expr" ]; then
        break
    fi
    
    calcul "$expr"
done
