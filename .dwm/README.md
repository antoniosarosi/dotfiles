![Dwm](../.screenshots/dwm.png)

***Language***
- [🇪🇸 Español](./README.es.md)
- 🇺🇸 English

My custom and patched build of **[dwm](https://dwm.suckless.org/)**.

Patches:
- [autostart](https://dwm.suckless.org/patches/autostart/dwm-autostart-20200610-cb3f58a.diff)
- [restartsig](https://dwm.suckless.org/patches/restartsig/dwm-restartsig-20180523-6.2.diff)
- [attachaside](https://dwm.suckless.org/patches/attachaside/dwm-attachaside-6.1.diff)
- [focusonactive](https://dwm.suckless.org/patches/focusonnetactive/dwm-focusonnetactive-6.2.diff)
- [warp](https://dwm.suckless.org/patches/warp/dwm-warp-6.2.diff)
- [rotatestack](https://dwm.suckless.org/patches/rotatestack/dwm-rotatestack-20161021-ab9571b.diff)
- [systray](https://dwm.suckless.org/patches/systray/dwm-systray-20200610-f09418b.diff)
- [scheme switch](https://dwm.suckless.org/patches/scheme_switch/dwm-scheme_switch-20170804-ceac8c9.diff)
- [fullgaps](https://dwm.suckless.org/patches/fullgaps/dwm-fullgaps-20200508-7b77734.diff)
- [gridmode](https://dwm.suckless.org/patches/gridmode/dwm-gridmode-20170909-ceac8c9.diff)
- [columns](https://dwm.suckless.org/patches/columns/dwm-columns-6.0.diff)
- [pertag](https://dwm.suckless.org/patches/pertag/)
- [cyclelayouts](https://dwm.suckless.org/patches/cyclelayouts/dwm-cyclelayouts-20180524-6.2.diff)

To install this on your system, first you need the following dependencies:

```bash
yay -S nerd-fonts-ubuntu-mono
```

I always use that font for icons.
You will also need my custom
**[dwmblocks](https://github.com/antoniosarosi/dotfiles/tree/master/.config/dwmblocks)**
and **[~/.local/bin](https://github.com/antoniosarosi/dotfiles/tree/master/.local/bin)**
scripts.

```bash
# dwm & dwmblocks
git clone https://github.com/antoniosarosi/dotfiles.git
cp -r dotfiles/.dwm ~
cp -r dotfiles/.config/dwmblocks ~/.config/

# scripts
cp dotfiles/.local/bin/percentage ~/.local/bin/
cp dotfiles/.local/bin/battery ~/.local/bin/
cp dotfiles/.local/bin/brightness ~/.local/bin/
cp dotfiles/.local/bin/volume ~/.local/bin/

# These scripts have some dependencies
sudo pacman -S pacman-contrib brightnessctl pamixer upower
```

Place this in your **~/.xprofile**:

```bash
export PATH=$HOME/.local/bin:$PATH
```

Build *dwm* and *dwmblocks* and create a new *xsession*:

```bash
cd ~/.dwm
sudo make clean install
cd ~/.config/dwmblocks/
sudo make clean install
sudo cp ~/.dwm/dwm.desktop /usr/share/xsessions
```

For *autostart*, check **~/.dwm/autostart.sh**.
Test it with **[Xephyr](https://wiki.archlinux.org/index.php/Xephyr)**:

```bash
Xephyr -br -ac -noreset -screen 1280x720 :1 &
DISPLAY=:1 dwm
```

If you want to modify bar icons, open **~/.config/dwmblocks/config.h**
and change these lines:

```cpp
static const Block blocks[] = {
//   Icon    Command                          Update Interval     Update Signal
    { "  ", "checkupdates | wc -l",                 60,               0 },
    { "",    "brightness",                           2,                0 },
    { "",    "volume",                               2,                0 },
    { "",    "battery",                              60,               0 },
    { "",    "date '+ %d/%m/%Y   %H:%M%p'",        5,                0 },
};
```

Then recompile *dwmblocks* and restart *dwm* using **mod + control + r**.

```bash
cd ~/.config/dwmblocks
sudo make clean install
```

Once that's done, you can login. But keep in mind keybindings will not work
unless you have the same programs that I use and the same configs. You can
either change keybindings or install the software I use and my config files,
check out [this section](https://github.com/antoniosarosi/dotfiles#keybindings)
for instructions.
