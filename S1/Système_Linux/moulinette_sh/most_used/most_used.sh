#!/bin/sh
#com de modif
cut -d " " -f1 ~/.bash_history | sort | uniq -c | sort -n -r | tr -s " " | cut -c2- | head -n 10

