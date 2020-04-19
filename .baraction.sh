#!/bin/bash
# baraction.sh for spectrwm status bar

# DATE
dte() {
  dte="$(date +"%d / %m / %Y - %H:%M")"
  echo -e "$dte"
}

# DISK
# hdd() {
#   hdd="$(df -h | awk 'NR==4{print $3, $5}')"
#   echo -e "HDD: $hdd"
# }

# RAM
mem() {
  mem=`free | awk '/Mem/ {printf "%d MiB/%d MiB\n", $3 / 1024.0, $2 / 1024.0 }'`
  echo -e "Mem: $mem"
}

# CPU
cpu() {
  read cpu a b c previdle rest < /proc/stat
  prevtotal=$((a+b+c+previdle))
  sleep 0.5
  read cpu a b c idle rest < /proc/stat
  total=$((a+b+c+idle))
  cpu=$((100*( (total-prevtotal) - (idle-previdle) ) / (total-prevtotal) ))
  echo -e "Cpu: $cpu%"
}

# Battery
bat() {
  bat=`upower -i /org/freedesktop/UPower/devices/battery_BAT1 | grep percentage | sed 's/ *percentage: *//g'`
  echo -e "Battery: $bat"
}

# Brightness
br() {
  br=`brightnessctl | grep Current | cut -d"(" -f2 | sed "s/)//"`
  echo -e "Brightness: $br"
}

# Volume
vol() {
  vol=`pamixer --get-volume`
  echo -e "Volume: $vol%"
}

SLEEP_SEC=5
#loops forever outputting a line every SLEEP_SEC secs
while :; do
    echo "$(cpu)    |    $(mem)    |    $(bat)    |    $(br)    |    $(vol)    |    $(dte)"
	sleep $SLEEP_SEC
done
