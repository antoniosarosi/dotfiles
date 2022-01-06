# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles

from libqtile import layout
from .theme import colors
from libqtile.config import Match

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
        *[Match(**rules) for rules in [
            {'wm_class': 'confirmreset'},
            {'wm_class': 'makebranch'},
            {'wm_class': 'maketag'},
            {'wm_class': 'ssh-askpass'},
            {'title': 'branchdialog'},
            {'title': 'pinentry'},
            {'wm_class': 'Arcolinux-welcome-app.py'},
            {'wm_class': 'Arcolinux-tweak-tool.py'},
            {'wm_class': 'Arcolinux-calamares-tool.py'},
            {'wm_class': 'makebranch'},
            {'wm_class': 'maketag'},
            {'wm_class': 'Arandr'},
            {'wm_class': 'feh'},
            {'wm_class': 'Galculator'},
            {'wm_class': 'arcolinux-logout'},
            {'wm_class': 'xfce4-terminal'},
            {'title': 'branchdialog'},
            {'title': 'Open File'},
        ]]
    ],
    border_focus=colors["color4"][0],
    full_screen_border_width=0,
)
