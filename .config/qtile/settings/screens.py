# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Multimonitor support

from libqtile.config import Screen
from libqtile import bar
from libqtile.log_utils import logger
from .widgets import primary_widgets, secondary_widgets
import subprocess


def status_bar(widgets):
    return bar.Bar(widgets, 24, opacity=0.8)


screens = [Screen(top=status_bar(primary_widgets()))]

# This is for my setup only, which has 3 different resolution monitors
# screens = [Screen(top=status_bar(secondary_widgets()))]
# screens.append(Screen(top=status_bar(secondary_widgets())))
# screens.append(Screen(top=bar.Bar(primary_widgets(), 39, opacity=0.8))) # 4K Monitor

xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"

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
    connected_monitors = int(command.stdout.decode("UTF-8"))

for _ in range(1, connected_monitors):
    screens.append(Screen(top=status_bar(secondary_widgets())))
