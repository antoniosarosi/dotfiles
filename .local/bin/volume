#!/bin/bash

vol=`pamixer --get-volume`

if [[ `pamixer --get-mute` == "true" ]]; then
    echo -n "ﱝ $vol% "
else
    echo -n "$(percentage $vol   奔 墳  ) $vol% "
fi
