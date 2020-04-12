from libqtile.config import Key, Group
from libqtile.command import lazy

from custom.bindings import mod_key

def init_groups(keys):
    groups = [Group(i) for i in ["NET", "DEV", "TERM", "FS", "MEDIA", "MISC"]]

    for i in range(len(groups)):
        # Each workspace is identified by a number starting at 1
        actual_key = i + 1
        keys.extend([
            # Switch to workspace N (actual_key)
            Key([mod_key], str(actual_key), lazy.group[groups[i].name].toscreen()),
            # Send window to workspace N (actual_key)
            Key([mod_key, "shift"], str(actual_key), lazy.window.togroup(groups[i].name)),
        ])

    return groups
