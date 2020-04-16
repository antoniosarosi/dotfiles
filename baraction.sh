#!/bin/bash
# baraction.sh for spectrwm status bar

## DATE
dte() {
  dte="$(date +"%d / %m / %Y  - %l:%M%p")"
  echo -e "$dte"
}

## DISK
# hdd() {
#   hdd="$(df -h | awk 'NR==4{print $3, $5}')"
#   echo -e "HDD: $hdd"
# }

## RAM
mem() {
  mem=`free | awk '/Mem/ {printf "%d MiB/%d MiB\n", $3 / 1024.0, $2 / 1024.0 }'`
  echo -e "MEM: $mem"
}

## CPU
cpu() {
  read cpu a b c previdle rest < /proc/stat
  prevtotal=$((a+b+c+previdle))
  sleep 0.5
  read cpu a b c idle rest < /proc/stat
  total=$((a+b+c+idle))
  cpu=$((100*( (total-prevtotal) - (idle-previdle) ) / (total-prevtotal) ))
  echo -e "CPU: $cpu%"
}

## Batery
bat() {
  bat=`upower -i /org/freedesktop/UPower/devices/battery_BAT1 | grep percentage | sed 's/ *percentage: *//g'`
  echo -e "Battery: $bat"
}

## Bright
br() {
  br=`brightnessctl | grep Current | sed "s/ *Current b/B/" | sed "s/\t//"`
  echo -e "$br"
}

## 

## VOLUME
# vol() {
#    vol=`amixer get Master | awk -F'[][]' 'END{ print $4":"$2 }'`
#    echo -e "VOL: $vol"
# }

SLEEP_SEC=5
#loops forever outputting a line every SLEEP_SEC secs
while :; do
    echo "$(cpu)    |    $(mem)    |    $(bat)    |    $(br)    |    $(dte)"
	sleep $SLEEP_SEC
done
