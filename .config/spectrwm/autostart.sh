#!/bin/bash

trayer \
    --edge top \
    --monitor 1 \
    --widthtype pixel \
    --width 100 \
    --heighttype pixel \
    --height 18 \
    --align right \
    --margin 390 \
    --transparent true \
    --alpha 0 \
    --tint 0x0F101A \
    --iconspacing 3 &

if [ -f ~/.theme/set-themes.py ]; then
    python ~/.theme/set-themes.py "spectrwm" &
fi

