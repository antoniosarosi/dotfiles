# Spectrwm

![Spectrwm](../../.screenshots/spectrwm.png)

Install spectrwm and dependencies:

```bash
sudo pacman -S spectrwm pacman-contrib trayer
yay -S nerd-fonts-ubuntu-mono
```

Clone this repository and copy my configs:

```bash
git clone https://github.com/antoniosarosi/dotfiles.git
cp -r dotfiles/.config/spectrwm ~/.config
cp dotfiles/.spectrwm.conf ~/.spectrwm.conf
```

Test it with **[Xephyr](https://wiki.archlinux.org/index.php/Xephyr)**:

```bash
Xephyr -br -ac -noreset -screen 1280x720 :1 &
DISPLAY=:1 spectrwm
```

Once that's done, you can login. But keep in mind keybindings will not work
unless you have the same programs that I use and the same configs. You can
either change keybindings or install the software I use and my config files,
check out [this section](https://github.com/antoniosarosi/dotfiles#keybindings)
for instructions.
