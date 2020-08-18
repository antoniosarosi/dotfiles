from libqtile import widget
from settings.theme import colors, img


base = lambda fg='text', bg='dark': {
    'foreground': colors[fg],
    'background': colors[bg]
}

separator = {
    **base(),
    'linewidth': 0,
    'padding': 5,
}

text_box = lambda fontsize=20: {
    'font': 'Ubuntu Mono',
    'fontsize': fontsize,
    'padding': 5
}

workspaces = lambda: [
    widget.Sep(**separator),
    widget.GroupBox(
        **base(fg='light'),
        font='UbuntuMono Nerd Font',
        fontsize=19,
        margin_y=3,
        margin_x=0,
        padding_y=8,
        padding_x=5,
        borderwidth=1,
        active=colors['active'],
        inactive=colors['inactive'],
        rounded=False,
        highlight_method='block',
        this_current_screen_border=colors['focus'],
        this_screen_border=colors['grey'],
        other_current_screen_border=colors['dark'],
        other_screen_border=colors['dark'],
        disable_drag=True
    ),
    widget.Sep(**separator),
    widget.WindowName(
        **base(fg='focus'),
        fontsize=14,
        padding=5
    ),
    widget.Sep(**separator),
]

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

laptop_widgets = [
    *workspaces(),
    widget.Systray(
        background=colors['dark'],
        padding=5
    ),
    widget.Sep(**separator),
    widget.Image(filename=img['bar4']),
    widget.TextBox(
        **base(bg='color4'),
        **text_box(25),
        text=' '  # Icon: nf-fa-download
    ),
    widget.Pacman(
        **base(bg='color4'),
        execute='alacritty',
        update_interval=1800
    ),
    widget.Image(
        filename=img['bar3']
    ),
    widget.TextBox(
        **base(bg='color3'),
        **text_box(25),
        text=' '  # Icon: nf-fa-feed
    ),
    widget.Net(
        **base(bg='color3'),
        interface='wlp2s0'
    ),
    widget.Image(
        filename=img['bar2']
    ),
    widget.CurrentLayoutIcon(
        **base(bg='color2'),
        scale=0.65
    ),
    widget.CurrentLayout(
        **base(bg='color2'),
        padding=5
    ),
    widget.Image(
        filename=img['bar1']
    ),
    widget.TextBox(
        **base(bg='color1'),
        **text_box(27),
        text=' '# Icon: nf-mdi-calendar_clock
    ),
    widget.Clock(
        **base(bg='color1'),
        format='%d/%m/%Y - %H:%M '
    ),
]

monitor_widgets = [
    *workspaces(),
    widget.Sep(**separator),
    widget.Image(
        filename=img['bar4']
    ),
    widget.CurrentLayoutIcon(
        **base(bg='color4'),
        scale=0.65
    ),
    widget.CurrentLayout(
        **base(bg='color4'),
        padding=5
    ),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
