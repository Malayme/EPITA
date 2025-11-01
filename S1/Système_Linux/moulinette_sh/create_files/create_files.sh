#!/bin/sh

touch " "
touch \\
touch -- --
touch \|
touch \"
touch \'
touch -- --\$\i\*\'\"\\
touch '# Exams are fun!'
touch ';`kill -9 0`'

for n in $(seq 1 50); do
    mkdir -p $(seq -s '/' 1 $n)
done

touch $(seq -s '/' 1 50)/farfaraway


