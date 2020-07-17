#!/usr/bin/env python

from sys import argv
from os import path
from notify import notification
import subprocess
import json


wm = argv[1]
home = path.expanduser("~")

with open(path.join(home, ".theme", "theme.json")) as f:
    theme = json.load(f)[wm]

subprocess.call([
    path.join(home, ".config", "alacritty", "theme.py"),
    theme["alacritty"]
])

if wm == "qtile":
    qtile_theme_file = path.join(
        path.expanduser("~"), ".config", "qtile", "config.json"
    )
    with open(qtile_theme_file) as f:
        qtile_config = json.load(f)
    qtile_config["theme"] = theme["wm"]
    with open(qtile_theme_file, "w") as f:
        json.dump(qtile_config, f)


notification("Theme set!", "Theme")
