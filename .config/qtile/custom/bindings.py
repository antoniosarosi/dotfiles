from libqtile.config import Key
from libqtile.command import lazy

mod_key = "mod4"

def init_keys():
    return [
        # ------------ WINDOW CONFIGS ------------

        # Switch between windows in current stack pane
        Key([mod_key], "j", lazy.layout.down()),
        Key([mod_key], "k", lazy.layout.up()),
        Key([mod_key], "h", lazy.layout.left()),
        Key([mod_key], "l", lazy.layout.right()),

        # Change window sizes (MonadTall)
        Key([mod_key, "shift"], "l", lazy.layout.grow()),
        Key([mod_key, "shift"], "h", lazy.layout.shrink()),

        # Toggle floating
        Key([mod_key, "shift"], "f", lazy.window.toggle_floating()),

        # Move windows up or down in current stack
        Key([mod_key, "shift"], "j", lazy.layout.shuffle_down()),
        Key([mod_key, "shift"], "k", lazy.layout.shuffle_up()),

        # Toggle between different layouts as defined below
        Key([mod_key], "Tab", lazy.next_layout()),

        # Kill window
        Key([mod_key], "w", lazy.window.kill()),

        # Restart Qtile
        Key([mod_key, "control"], "r", lazy.restart()),

        Key([mod_key, "control"], "q", lazy.shutdown()),
        Key([mod_key], "r", lazy.spawncmd()),

        # Switch window focus to other pane(s) of stack
        Key([mod_key], "space", lazy.layout.next()),

        # Swap panes of split stack
        Key([mod_key, "shift"], "space", lazy.layout.rotate()),

        # ------------ APPS CONFIG ------------

        # Menu
        Key([mod_key], "m", lazy.spawn("rofi -show run")),

        # Window Nav
        Key([mod_key, "shift"], "m", lazy.spawn("rofi -show")),

        # Browser
        Key([mod_key], "b", lazy.spawn("firefox")),

        # File Manager
        Key([mod_key], "f", lazy.spawn("thunar")),

        # Terminal
        Key([mod_key], "Return", lazy.spawn("alacritty")),

        # Redshift
        Key([mod_key], "r", lazy.spawn("redshift -O 2400")),
        Key([mod_key, "shift"], "r", lazy.spawn("redshift -x")),

        # ------------ HARDWARE CONFIG ------------

        # Volume
        Key([], "XF86AudioLowerVolume", lazy.spawn(
            "pactl set-sink-volume @DEFAULT_SINK@ -5%"
        )),
        Key([], "XF86AudioRaiseVolume", lazy.spawn(
            "pactl set-sink-volume @DEFAULT_SINK@ +5%"
        )),
        Key([], "XF86AudioMute", lazy.spawn(
            "pactl set-sink-mute @DEFAULT_SINK@ toggle"
        )),

        #Brightness
        Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
        Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
    ]
