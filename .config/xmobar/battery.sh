bat=`upower -i /org/freedesktop/UPower/devices/battery_BAT1 |
    grep percentage |
    sed 's/ *percentage: *//g'`

percentage=`echo $bat | sed 's/%//'`

if (( $percentage <= 25 )); then
    echo -n "  $bat" 
elif (( $percentage <= 50 )); then
    echo -n "  $bat"
elif (( $percentage <= 75 )); then
    echo -n "  $bat" 
else
    echo -n "  $bat"
fi
