# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Theming for Qtile

from os import listdir
from os import path
import subprocess
import json

from settings.path import qtile_path


default_theme = "dark-grey"

with open(path.join(qtile_path, "config.json")) as f:
    theme = json.load(f)["theme"]

theme_path = path.join(qtile_path, "themes", theme)
if not path.isdir(theme_path):
    theme_path = path.join(qtile_path, "themes", default_theme)

# Map color name to hex values
with open(path.join(theme_path, "colors.json")) as f:
    colors = json.load(f)
