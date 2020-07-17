# Qtile Config File
# http://www.qtile.org/

# Antonio Sarosi
# https://www.youtube.com/c/antoniosarosi


from libqtile import hook

from settings.keys import mod, keys
from settings.groups import groups
from settings.layouts import layouts, floating_layout
from settings.widgets import widget_defaults, extension_defaults
from settings.screens import screens
from settings.mouse import mouse

from os import path
import subprocess


@hook.subscribe.startup_once
def autostart():
    subprocess.call([
        path.join(path.expanduser('~'), '.config', 'qtile', 'autostart.sh')
    ])


main = None
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = 'smart'
wmname = 'LG3D'
