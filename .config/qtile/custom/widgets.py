from libqtile import widget
from custom.theme import colors, img

def init_widgets():
    return [
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors["light"],
            background=colors["dark"]
        ),
        widget.GroupBox(
            font="Ubuntu Bold",
            fontsize=10,
            margin_y=0,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors["light"],
            inactive=colors["light"],
            rounded=False,
            highlight_method="block",
            this_current_screen_border=colors["primary"],
            this_screen_border=colors ["grey"],
            other_current_screen_border=colors["dark"],
            other_screen_border=colors["dark"],
            foreground=colors["light"],
            background=colors["dark"]
        ),
        widget.Sep(
            linewidth=0,
            padding=10,
            foreground=colors["light"],
            background=colors["dark"]
        ),
        widget.WindowName(
            font="Ubuntu Bold",
            fontsize=11,
            foreground=colors["primary"],
            background=colors["dark"],
            padding=5
        ),
        widget.Sep(
            linewidth=0,
            padding=5,
            foreground=colors["light"],
            background=colors["dark"]
        ),
        widget.Systray(
            background=colors["dark"],
            padding=5
        ),
        widget.Sep(
            linewidth=0,
            padding=5,
            foreground=colors["light"],
            background=colors["dark"]
        ),
        widget.Image(
            scale=True,
            filename=img["bg-to-secondary"],
            background=colors["dark"]
        ),
        widget.TextBox(
            font="Ubuntu Bold",
            text=" ⟳",
            padding=5,
            foreground=colors["light"],
            background=colors["secondary"],
            fontsize=15
        ),
        widget.Pacman(
            execute="alacritty",
            update_interval=1800,
            foreground=colors["light"],
            background=colors["secondary"]
        ),
        widget.Image(
            scale=True,
            filename=img["primary"],
            background=colors["dark"]
        ),
        widget.TextBox(
            text=" ↯",
            foreground=colors["light"],
            background=colors["primary"],
            padding=5,
            fontsize=15
        ),
        widget.Net(
            interface="wlp2s0",
            foreground=colors["light"],
            background=colors["primary"],
        ),
        widget.Image(
            scale=True,
            filename=img["secondary"],
            background=colors["dark"]
        ),
        widget.CurrentLayoutIcon(
            scale=0.65,
            foreground=colors["light"],
            background=colors["secondary"],
        ),
        widget.CurrentLayout(
            foreground=colors["light"],
            background=colors["secondary"],
            padding=5
        ),
        widget.Image(
            scale=True,
            filename=img["primary"],
            background=colors["dark"]
        ),
        widget.TextBox(
            font="Ubuntu Bold",
            text=" 🕒",
            foreground=colors["light"],
            background=colors["primary"],
            padding=5,
            fontsize=15
        ),
        widget.Clock(
            foreground=colors["light"],
            background=colors["primary"],
            format="%d / %m / %Y - %H:%M "
        ),
    ]


defaults = dict(
    font='Ubuntu Mono',
    fontsize=13,
    padding=2,
)
