from libqtile import widget
from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=2)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark", fontsize=60, padding=5):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=fontsize,
        padding=padding
    )


def workspaces(icon_fontsize=19, window_name_font_size=14): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=icon_fontsize,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=window_name_font_size, padding=0),
        separator(),
    ]


# TODO: Ugly Hack to make the bar on a 27" 4K monitor have normal size. Needs refactoring.
# def primary_widgets():
#     return [
#         *workspaces(28, 22),

#         separator(),

#         powerline('color4', 'dark', 54, -4),

#         icon(bg="color4", text=' ', fontsize=20), # Icon: nf-fa-download

#         widget.CheckUpdates(
#             background=colors['color4'],
#             colour_have_updates=colors['text'],
#             colour_no_updates=colors['text'],
#             no_update_string='0',
#             display_format='{updates}',
#             update_interval=1800,
#             custom_command='checkupdates',
#             fontsize=20
#         ),

#         powerline('color3', 'color4', 54, -4),

#         icon(bg="color3", text=' ', fontsize=20),  # Icon: nf-fa-feed

#         widget.Net(**base(bg='color3'), interface='wlo1', fontsize=20),

#         powerline('color2', 'color3', 54, -4),

#         widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),

#         widget.CurrentLayout(**base(bg='color2'), padding=5, fontsize=20),

#         powerline('color1', 'color2', 54, -4),

#         icon(bg="color1", fontsize=20, text=' '), # Icon: nf-mdi-calendar_clock

#         widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M ', fontsize=20),

#         powerline('dark', 'color1', 54, -4),

#         widget.Systray(background=colors['dark'], padding=5, icon_size=40),
#     ]

def primary_widgets():
    return [
        *workspaces(),

        separator(),

        powerline('color4', 'dark'),

        icon(bg="color4", text=' '), # Icon: nf-fa-download

        widget.CheckUpdates(
            background=colors['color4'],
            colour_have_updates=colors['text'],
            colour_no_updates=colors['text'],
            no_update_string='0',
            display_format='{updates}',
            update_interval=1800,
            custom_command='checkupdates',
        ),

        powerline('color3', 'color4'),

        icon(bg="color3", text=' '),  # Icon: nf-fa-feed

        widget.Net(**base(bg='color3'), interface='wlo1'),

        powerline('color2', 'color3'),

        widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),

        widget.CurrentLayout(**base(bg='color2')),

        powerline('color1', 'color2'),

        icon(bg="color1", text=' '), # Icon: nf-mdi-calendar_clock

        widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),

        powerline('dark', 'color1'),

        widget.Systray(background=colors['dark']),
    ]


def secondary_widgets():
    return [
        *workspaces(),

        separator(),

        powerline('color1', 'dark'),

        widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

        widget.CurrentLayout(**base(bg='color1'), padding=4),

        powerline('color2', 'color1'),

        icon(bg="color2", text=' '), # Icon: nf-mdi-calendar_clock

        widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

        powerline('dark', 'color2'),
    ]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 14,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
