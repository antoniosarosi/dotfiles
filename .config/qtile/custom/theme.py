from os import listdir
from os import path
import json


# color scheme available in ~/.config/qtile/themes
theme = "material-darker"

theme_path = path.join(
    path.expanduser("~"), ".config", "qtile", "themes", theme
)

# map color name to hex values
with open(path.join(theme_path, "colors.json")) as f:
    colors = json.load(f)

img = {}

# map img name to its path
img_path = path.join(theme_path, "img")
for i in listdir(img_path):
    img[i.split(".")[0]] = path.join(img_path, i)
