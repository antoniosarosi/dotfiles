# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

# Theming for Qtile

from os import path
import subprocess
import json

from settings.path import qtile_path


default_theme = "dark-grey"

with open(path.join(qtile_path, "config.json")) as f:
    theme = json.load(f)["theme"]

theme_file = path.join(qtile_path, "themes", f'{theme}.json')
if not path.isfile(theme_file):
    theme_file = path.join(qtile_path, "themes", f'{default_theme}.json')

# Map color name to hex values
with open(path.join(theme_file)) as f:
    colors = json.load(f)
