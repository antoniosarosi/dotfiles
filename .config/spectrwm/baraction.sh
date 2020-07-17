#!/bin/bash
# baraction.sh for spectrwm status bar

icon() {
    echo -n "+@fg=1;$1+@fg=0;"
}

percentage() {
    current=`echo $1 | sed 's/%//'`
    if [ $current -le 25 ]; then 
        echo -n "$(icon $2)"
    elif [ $current -le 50 ]; then
        echo -n "$(icon $3)"
    elif [ $current -le 75 ]; then
        echo -n "$(icon $4)"
    else
        echo -n "$(icon $5)"
    fi
}

# Date
dte() {
    dte="$(date +"$(icon  ) %d/%m/%Y $(icon  ) %H:%M")"
    echo -e "$dte"
}

# Disk
# hdd() {
#     hdd="$(df -h | awk 'NR==4{print $3, $5}')"
#     echo -e "HDD: $hdd"
# }

# Ram
# mem() {
#     mem=`free | awk '/Mem/ {printf "%d MiB/%d MiB\n", $3 / 1024.0, $2 / 1024.0 }'`
#     echo -e "Mem: $mem"
# }

# Cpu
# cpu() {
#     read cpu a b c previdle rest < /proc/stat
#     prevtotal=$((a + b + c + previdle))
#     sleep 0.5
#     read cpu a b c idle rest < /proc/stat
#     total=$((a + b + c + idle))
#     cpu=$((100 * ((total - prevtotal) - (idle - previdle) ) / (total - prevtotal)))
#     echo -e "Cpu: $cpu%"
# }

# Battery
bat() {
    bat=`upower -i /org/freedesktop/UPower/devices/battery_BAT1 | 
        grep percentage |
        sed 's/ *percentage: *//g'`
    echo -n "$(percentage $bat            )  $bat"
}

# Brightness
br() {
    br=`brightnessctl | grep Current | cut -d"(" -f2 | sed "s/)//"`
    echo -n "$(percentage $br        ) $br"
}

# Volume
vol() {
    vol=`pamixer --get-volume`
    if [[ `pamixer --get-mute` == "true" ]]; then
        echo -n "$(icon ﱝ ) $vol"
    else
        echo -n "$(percentage $vol   奔 墳   ) $vol%"
    fi
}

SLEEP_SEC=1
while :; do
    echo -n "$(br) "
    echo -n "$(vol) "
    echo -n "$(bat) "
    echo "$(dte)"
	sleep $SLEEP_SEC
done
