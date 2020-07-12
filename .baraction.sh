#!/bin/bash
# baraction.sh for spectrwm status bar

# DATE
dte() {
  dte="$(date +"%d/%m/%Y - %H:%M")"
  echo -e "$dte"
}

# DISK
# hdd() {
#   hdd="$(df -h | awk 'NR==4{print $3, $5}')"
#   echo -e "HDD: $hdd"
# }

# RAM
# mem() {
#   mem=`free | awk '/Mem/ {printf "%d MiB/%d MiB\n", $3 / 1024.0, $2 / 1024.0 }'`
#   echo -e "Mem: $mem"
# }

# CPU
# cpu() {
#   read cpu a b c previdle rest < /proc/stat
#   prevtotal=$((a + b + c + previdle))
#   sleep 0.5
#   read cpu a b c idle rest < /proc/stat
#   total=$((a + b + c + idle))
#   cpu=$((100 * ((total - prevtotal) - (idle - previdle) ) / (total - prevtotal)))
#   echo -e "Cpu: $cpu%"
# }

# Battery
bat() {
  bat=`upower -i /org/freedesktop/UPower/devices/battery_BAT1 | grep percentage | sed 's/ *percentage: *//g'`
  echo -e "$bat"
}

# Brightness
br() {
  br=`brightnessctl | grep Current | cut -d"(" -f2 | sed "s/)//"`
  echo -e "$br"
}

# Volume
vol() {
  vol=`pamixer --get-volume`
  echo -e "$vol%"
}

SLEEP_SEC=1
while :; do
    echo -n "+@fg=1;+@fn=0;☀+@fn=1;+@fg=0; $(br) "
    echo -n "+@fg=1;+@fn=0;🔊+@fn=1;+@fg=0; $(vol) "
    echo -n "+@fg=1;⚡+@fg=0; $(bat) "
    echo "+@fg=1;+@fn=0;⏲+@fn=1;+@fg=0; $(dte)"
	sleep $SLEEP_SEC
done
