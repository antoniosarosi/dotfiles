#!/bin/bash

if [ $# -lt 5 ]; then
    echo "Missing args, usage: percentage current icon1 icon2 icon3 icon4"
    exit 1
fi

current=`echo $1 | sed 's/%//'`
if [ $current -le 25 ]; then 
    echo -n $2
elif [ $current -le 50 ]; then
    echo -n $3
elif [ $current -le 75 ]; then
    echo -n $4
else
    echo -n $5
fi
