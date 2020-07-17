from libqtile.config import Key, Group
from libqtile.command import lazy
from settings.keys import mod, keys


# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)
# Icons: 
# nf-fa-firefox, 
# nf-fa-code_fork, 
# nf-dev-terminal, 
# nf-mdi-folder, 
# nf-mdi-image, 
# nf-mdi-layers

groups = [Group(i) for i in ["   ", "  ", "   ", "   ", "   ", "   "]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        # Switch to workspace N
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        # Send window to workspace N
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])
