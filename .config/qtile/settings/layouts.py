# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

from libqtile import layout
from .theme import colors

# Layouts and layout rules


layout_conf = {
    'border_focus': colors['focus'][0],
    'border_width': 1,
    'margin': 8
}

layouts = [
    layout.Max(),
    layout.MonadTall(**layout_conf),
    layout.MonadWide(**layout_conf),
    layout.Bsp(**layout_conf),
    layout.Matrix(columns=2, **layout_conf),
    layout.RatioTile(**layout_conf),
    # layout.Columns(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        {'wm_class': 'confirmreset'},
        {'wm_class': 'makebranch'},
        {'wm_class': 'maketag'},
        {'wm_class': 'ssh-askpass'},
        {'title': 'branchdialog'},
        {'title': 'pinentry'},
        {'wmclass': 'Arcolinux-welcome-app.py'},
        {'wmclass': 'Arcolinux-tweak-tool.py'},
        {'wmclass': 'Arcolinux-calamares-tool.py'},
        {'wmclass': 'makebranch'},
        {'wmclass': 'maketag'},
        {'wmclass': 'Arandr'},
        {'wmclass': 'feh'},
        {'wmclass': 'Galculator'},
        {'wmclass': 'arcolinux-logout'},
        {'wmclass': 'xfce4-terminal'},
        {'wname': 'branchdialog'},
        {'wname': 'Open File'},
    ],
    border_focus=colors["color4"][0],
    full_screen_border_width=0,
)
