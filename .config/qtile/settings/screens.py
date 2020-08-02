from libqtile.config import Screen
from libqtile import bar
from settings.widgets import laptop_widgets, monitor_widgets
import subprocess


status_bar = lambda widgets: bar.Bar(widgets, 24, opacity=0.95)

screens = [Screen(top=status_bar(laptop_widgets))]

connected_monitors = subprocess.run(
    "xrandr | grep 'connected' | cut -d ' ' -f 2",
    shell=True,
    stdout=subprocess.PIPE
).stdout.decode("UTF-8").split("\n")[:-1].count("connected")

if connected_monitors > 1:
    for i in range(1, connected_monitors):
        screens.append(Screen(top=status_bar(monitor_widgets)))
