from libqtile.config import Screen
from libqtile import bar

from custom.widgets import init_widgets
import subprocess


def create_screen():
    return Screen(
        top=bar.Bar(
            init_widgets(),
            24,
            opacity=0.95
        )
    )


def init_screens():
    screens = [create_screen()]

    # Check if HMDI is plugged in, if so initialize another screen
    check_hdmi = "xrandr | grep ' connected' | grep 'HDMI' | awk '{print $1}'"
    if (subprocess.getoutput(check_hdmi) == "HDMI-1"):
        screens.append(create_screen())

    return screens
