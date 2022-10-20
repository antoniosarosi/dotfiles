# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Multimonitor support

import subprocess

from libqtile import bar
from libqtile.config import Screen
from libqtile.log_utils import logger

from .widgets import primary_widgets, secondary_widgets


def status_bar(widgets):
    return bar.Bar(widgets, 24, opacity=1)


screens = [Screen(top=status_bar(primary_widgets()))]

xrandr = "xrandr | grep -w 'connected'"

command = subprocess.run(
    xrandr,
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

if command.returncode != 0:
    error = command.stderr.decode("UTF-8")
    logger.error(f"Failed counting monitors using {xrandr}:\n{error}")
    connected_monitors = 1
else:
    # Check the output of the xrandr command, if a monitor is connected
    # but turned off, then it will not show any resolution for that montior.
    xrandr_output = command.stdout.decode("UTF-8").split("\n")[:-1]
    resolutions = map(lambda output: output.split(" ")[2], xrandr_output) 
    connected_monitors = len([r for r in resolutions if not r.startswith("(")])

# This is for my setup only, which has 3 different resolution monitors
# if connected_monitors == 3:
#     screens = [Screen(top=status_bar(secondary_widgets()))]
#     screens.append(Screen(top=status_bar(secondary_widgets())))
#     screens.append(Screen(top=bar.Bar(primary_widgets(), 39, opacity=1))) # 4K Monitor
# elif connected_monitors == 2:
#     screens = [Screen(top=status_bar(secondary_widgets()))]
#     screens.append(Screen(top=bar.Bar(primary_widgets(), 39, opacity=1))) # 4K Monitor

for _ in range(1, connected_monitors):
    screens.append(Screen(top=status_bar(secondary_widgets())))
