from libqtile import hook

from os import path
import subprocess

@hook.subscribe.startup_once
def autostart():
    script = path.join(
        path.expanduser("~"), ".config", "qtile", "autostart.sh"
    )
    subprocess.call([script])
