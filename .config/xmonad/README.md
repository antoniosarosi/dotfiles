# Xmonad

![Xmonad](../../.screenshots/xmonad.png)

***Language***
- [🇪🇸 Español](./README.es.md)
- 🇺🇸 English

## Installation

This is how to setup *Xmonad* using this config:

```bash
# First, install packages and dependencies
sudo pacman -S xmonad xmonad-contrib xmobar trayer xdotool
yay -S nerd-fonts-ubuntu-mono

# Clone this respository and copy my configs
git clone https://github.com/antoniosarosi/dotfiles.git
cp -r dotfiles/.config/xmonad ~/.config
cp -r dotfiles/.config/xmobar ~/.config
```

*Xmobar* will not work if you don't have my
**[~/.local/bin](https://github.com/antoniosarosi/dotfiles/tree/master/.local/bin)**
scripts.

```bash
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

Compile *Xmonad* and you should be able to login or test it with
**[Xephyr](https://wiki.archlinux.org/index.php/Xephyr)**:

```bash
xmonad --recompile
Xephyr -br -ac -noreset -screen 1280x720 :1 &
DISPLAY=:1 xmonad
```

## Xmobar

If it launches *Xmobar*, you know that the setup is correct. Modify 
*Xmobar* instances according to how many monitors you have. This is how
I set them up:

```haskell
main = do
    -- Xmobar
    xmobarLaptop <- spawnPipe "xmobar -x 0 ~/.config/xmobar/primary.hs"
    xmobarMonitor <- spawnPipe "xmobar -x 1 ~/.config/xmobar/secondary.hs"
```

For example, if you only need one bar then remove the line with *xmobarMonitor*.
If you want 3 bars, copy and paste that line and change the name of the third
bar. You also need to modify the following line if you need a third *Xmobar*
or if you want to remove the second one.

```haskell
ppOutput = \x -> hPutStrLn xmobarLaptop x >> hPutStrLn xmobarMonitor x,
```

Only one bar:

```haskell
ppOutput = \x -> hPutStrLn xmobarLaptop x
```

Three bars:

```haskell
ppOutput = \x -> hPutStrLn xmobarLaptop x >> hPutStrLn xmobarMonitor1 x >> hPutStrLn xmobarMonitor2 x,
```

If the battery doesn't work (if you're on a laptop, obviously), look for this
line in **~/.local/bin/battery**:

```bash
bat=`upower -i /org/freedesktop/UPower/devices/battery_BAT1 |
    grep percentage |
    sed 's/ *percentage: *//g'`
```

You might need to change *battery_BAT1* to the value you see in this output:

```bash
upower -d
```

Once that's done, you can login. But keep in mind keybindings will not work
unless you have the same programs that I use and the same configs. You can
either change keybindings or install the software I use and my config files,
check out [this section](https://github.com/antoniosarosi/dotfiles#keybindings)
for instructions.

## Autostart

You can find these lines in **./xmonad.hs**:

```haskell
myStartupHook :: X ()
myStartupHook = do
    spawnOnce "trayer --edge top  --monitor 1 --widthtype pixel --width 40 --heighttype pixel --height 18 --align right --transparent true --alpha 0 --tint 0x292d3e --iconspacing 3 --distance 1 &"
    setWMName "LG3D"
```

I don't have a bash script for launching programs, because I only use *trayer*,
but if you want one, you can do something like:

```bash
touch ~/.xmonad/autostart.sh
chmod u+x ~/.xmonad/autostart.sh
```

Now put what you need in that file, and change the previous lines to:

```haskell
myStartupHook :: X ()
myStartupHook = do
    spawnOnce "/home/username/.xmonad/autostart.sh &"
    setWMName "LG3D"
```
