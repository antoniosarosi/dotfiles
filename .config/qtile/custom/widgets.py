# Reusable configs for Widgets, necessary for displaying different
# widgets on different screens

from libqtile import widget
from custom.theme import colors, img


def base(fg='light', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


# Custom configs for each widget

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

defaults = {
    'font': 'Ubuntu Mono',
    'fontsize': 13,
    'padding': 2
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


def init_laptop_widgets():
    return [
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


def init_monitor_widgets():
    return [
        *workspaces(),
        widget.Image(
            filename=img['bg-to-secondary']
        ),
        *powerline_base()
    ]
