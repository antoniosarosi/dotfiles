from os import listdir
from os import path
import subprocess
import json

from settings.path import home, qtile_path


default_theme = "dark-grey"

theme_setup_script = path.join(home, ".theme", "set-themes.py")
if path.isfile(theme_setup_script):
    subprocess.call([theme_setup_script, "qtile"])

with open(path.join(qtile_path, "config.json")) as f:
    theme = json.load(f)["theme"]

theme_path = path.join(qtile_path, "themes", theme)
if not path.isdir(theme_path):
    theme_path = path.join(qtile_path, "themes", default_theme)

# Map color name to hex values
with open(path.join(theme_path, "colors.json")) as f:
    colors = json.load(f)

img = {}

# Map image name to its path
img_path = path.join(theme_path, "img")
for i in listdir(img_path):
    img[i.split(".")[0]] = path.join(img_path, i)
