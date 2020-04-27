# Qtile Config File
# http://www.qtile.org/

# Antonio Sarosi
# https://www.youtube.com/channel/UCzTi9I3zApECTkukkMOpEEA/featured

# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook

from os import listdir
from os import path
import subprocess
import json


qtile_path = path.join(path.expanduser("~"), ".config", "qtile")


# THEME

theme = "material-darker" # only if available in ~/.config/qtile/themes

theme_path = path.join(qtile_path, "themes", theme)

# map color name to hex values
with open(path.join(theme_path, "colors.json")) as f:
    colors = json.load(f)

img = {}

# map image name to its path
img_path = path.join(theme_path, "img")
for i in listdir(img_path):
    img[i.split(".")[0]] = path.join(img_path, i)


# AUTOSTART

@hook.subscribe.startup_once
def autostart():
    script = path.join(qtile_path, "autostart.sh")
    subprocess.call([script])


# KEYS

mod = "mod4"

#          Special  KeyCap  Actions
keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Window Configs ------------

    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # Switch window focus to other pane(s) of stack
    ([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    ([mod, "shift"], "space", lazy.layout.rotate()),

    # ------------ Apps Configs ------------

    # Menu
    ([mod], "m", lazy.spawn("rofi -show run")),

    # Window Nav
    ([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser
    ([mod], "b", lazy.spawn("firefox")),

    # File Manager
    ([mod], "f", lazy.spawn("thunar")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),

    # Redshift
    ([mod], "r", lazy.spawn("redshift -O 2400")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # ------------ Hardware Configs ------------

    # Volume
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    #Brightness
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]


# GROUPS

groups = [Group(i) for i in ["NET", "DEV", "TERM", "FS", "MEDIA", "MISC"]]

for i, group in enumerate(groups):
    # Each workspace is identified by a number starting at 1
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N (actual_key)
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N (actual_key)
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])


# LAYOUTS

layout_conf = {
    'border_focus': colors['primary'][0],
    'border_width': 1,
    'margin': 4
}

layouts = [
    layout.Max(),
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
    layout.Matrix(columns=2, **layout_conf),
    # layout.Bsp(),
    # layout.Columns(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


# WIDGETS

# Reusable configs for displaying different widgets on different screens

def base(fg='light', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


separator = {
    **base(),
    'linewidth': 0,
    'padding': 5,
}

group_box = {
    **base(),
    'font': 'Ubuntu Bold',
    'fontsize': 10,
    'margin_y': 5,
    'margin_x': 0,
    'padding_y': 8,
    'padding_x': 5,
    'borderwidth': 1,
    'active': colors['light'],
    'inactive': colors['light'],
    'rounded': False,
    'highlight_method': 'block',
    'this_current_screen_border': colors['primary'],
    'this_screen_border': colors['grey'],
    'other_current_screen_border': colors['dark'],
    'other_screen_border': colors['dark']
}

window_name = {
    **base(fg='primary'),
    'font': 'Ubuntu Bold',
    'fontsize': 11,
    'padding': 5
}

systray = {
    'background': colors['dark'],
    'padding': 5
}

text_box = {
    'font': 'Ubuntu Bold',
    'fontsize': 15,
    'padding': 5
}

pacman = {
    'execute': 'alacritty',
    'update_interval': 1800
}

net = {
    'interface': 'wlp2s0'
}

current_layout_icon = {
    'scale': 0.65
}

current_layout = {
    'padding': 5
}

clock = {
    'format': '%d / %m / %Y - %H:%M '
}


def workspaces():
    return [
        widget.Sep(**separator),
        widget.GroupBox(**group_box),
        widget.Sep(**separator),
        widget.WindowName(**window_name)
    ]


def powerline_base():
    return [
        widget.CurrentLayoutIcon(
            **base(bg='secondary'),
            **current_layout_icon
        ),
        widget.CurrentLayout(
            **base(bg='secondary'),
            **current_layout
        ),
        widget.Image(
            filename=img['primary']
        ),
        widget.TextBox(
            **base(bg='primary'),
            **text_box,
            text=' 🕒'
        ),
        widget.Clock(
            **base(bg='primary'),
            **clock
        )
    ]


laptop_widgets = [
    *workspaces(),

    widget.Sep(
        **separator
    ),
    widget.Systray(
        **systray
    ),
    widget.Sep(
        **separator
    ),
    widget.Image(
        filename=img['bg-to-secondary']
    ),
    widget.TextBox(
        **base(bg='secondary'),
        **text_box,
        text=' ⟳'
    ),
    widget.Pacman(
        **base(bg='secondary'),
        **pacman
    ),
    widget.Image(
        filename=img['primary']
    ),
    widget.TextBox(
        **base(bg='primary'),
        **text_box,
        text=' ↯'
    ),
    widget.Net(
        **base(bg='primary'),
        **net
    ),
    widget.Image(
        filename=img['secondary']
    ),
    *powerline_base()
 ]


monitor_widgets = [
    *workspaces(),
    widget.Image(
        filename=img['bg-to-secondary']
    ),
    *powerline_base()
]

widget_defaults = {
    'font': 'Ubuntu Mono',
    'fontsize': 13,
    'padding': 2
}
extension_defaults = widget_defaults.copy()


# SCREENS

screens = [
    Screen(top=bar.Bar(laptop_widgets, 24, opacity=0.95))
]

# check connected monitors
monitors_status = subprocess.run(
    "xrandr | grep 'connected' | cut -d ' ' -f 2",
    shell=True,
    stdout=subprocess.PIPE
).stdout.decode("UTF-8").split("\n")[:-1]

if monitors_status.count("connected") == 2:
    screens.append(
        Screen(top=bar.Bar(monitor_widgets, 24, opacity=0.95))
    )


# MOUSE

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]


# OTHER STUFF

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        {'wmclass': 'confirm'},
        {'wmclass': 'dialog'},
        {'wmclass': 'download'},
        {'wmclass': 'error'},
        {'wmclass': 'file_progress'},
        {'wmclass': 'notification'},
        {'wmclass': 'splash'},
        {'wmclass': 'toolbar'},
        {'wmclass': 'confirmreset'},  # gitk
        {'wmclass': 'makebranch'},  # gitk
        {'wmclass': 'maketag'},  # gitk
        {'wname': 'branchdialog'},  # gitk
        {'wname': 'pinentry'},  # GPG key password entry
        {'wmclass': 'ssh-askpass'},  # ssh-askpass
    ],
    border_focus=colors["secondary"][0]
)
auto_fullscreen = True
focus_on_window_activation = "smart"

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's lightlist.
wmname = "LG3D"
