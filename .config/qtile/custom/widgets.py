from libqtile import widget
from custom.theme import colors, img


def sep(p):
    return widget.Sep(
        linewidth=0,
        padding=p,
        foreground=colors["light"],
        background=colors["dark"]
    )


def group_box():
    return widget.GroupBox(
        font="Ubuntu Bold",
        fontsize=10,
        margin_y=5,
        margin_x=0,
        padding_y=8,
        padding_x=5,
        borderwidth=1,
        active=colors["light"],
        inactive=colors["light"],
        rounded=False,
        highlight_method="block",
        this_current_screen_border=colors["primary"],
        this_screen_border=colors["grey"],
        other_current_screen_border=colors["dark"],
        other_screen_border=colors["dark"],
        foreground=colors["light"],
        background=colors["dark"]
    )


def window_name():
    return widget.WindowName(
        font="Ubuntu Bold",
        fontsize=11,
        foreground=colors["primary"],
        background=colors["dark"],
        padding=5
    )


def systray():
    return widget.Systray(
        background=colors["dark"],
        padding=5
    )


def image(image):
    return widget.Image(
        scale=True,
        filename=img[image],
        background=colors["dark"]
    )


def text_box(s, bgcolor):
    return widget.TextBox(
        font="Ubuntu Bold",
        text=s,
        padding=5,
        foreground=colors["light"],
        background=colors[bgcolor],
        fontsize=15
    )


def pacman(bgcolor):
    return widget.Pacman(
        execute="alacritty",
        update_interval=1800,
        foreground=colors["light"],
        background=colors[bgcolor]
    )


def net(bgcolor):
    return widget.Net(
        interface="wlp2s0",
        foreground=colors["light"],
        background=colors[bgcolor],
    )


def current_layout_icon(bgcolor):
    return widget.CurrentLayoutIcon(
        scale=0.65,
        foreground=colors["light"],
        background=colors[bgcolor],
    )


def current_layout(bgcolor):
    return widget.CurrentLayout(
        foreground=colors["light"],
        background=colors[bgcolor],
        padding=5
    )


def clock(bgcolor):
    return widget.Clock(
        foreground=colors["light"],
        background=colors[bgcolor],
        format="%d / %m / %Y - %H:%M "
    )


def init_laptop_widgets():
    return [
        sep(5),
        group_box(),
        sep(5),
        window_name(),
        sep(5),
        systray(),
        sep(5),
        image("bg-to-secondary"),
        text_box(" ⟳", "secondary"),
        pacman("secondary"),
        image("primary"),
        text_box(" ↯", "primary"),
        net("primary"),
        image("secondary"),
        current_layout_icon("secondary"),
        current_layout("secondary"),
        image("primary"),
        text_box(" 🕒", "primary"),
        clock("primary")
     ]


def init_monitor_widgets():
    return [
        sep(5),
        group_box(),
        sep(5),
        window_name(),
        image("bg-to-secondary"),
        current_layout_icon("secondary"),
        current_layout("secondary"),
        image("primary"),
        text_box(" 🕒", "primary"),
        clock("primary")
    ]


defaults = dict(
    font='Ubuntu Mono',
    fontsize=13,
    padding=2,
)
