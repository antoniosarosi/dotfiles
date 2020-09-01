# Xmonad

![Xmonad](../.screenshots/xmonad.png)

Language
[🇪🇸](./README.es.md)
🇺🇸

This is how to setup *Xmonad* using this config:

```bash
# First, install packages and dependencies
sudo pacman -S xmonad xmonad-contrib xmobar trayer
yay -S nerd-fonts-ubuntu-mono

# Clone this respository and copy my configs
git clone https://github.com/antoniosarosi/dotfiles.git
cp -r dotfiles/.xmonad ~
cp -r dotfiles/.config/xmobar ~/.config
```

Compile *Xmonad* and you should be able to login or test it with
**[Xephyr](https://wiki.archlinux.org/index.php/Xephyr)**:

```bash
xmonad --recompile
Xephyr -br -ac -noreset -screen 1280x720 :1 &
DISPLAY=:1 xmonad
```

If it launches *Xmobar*, you know that the setup is correct. Modify 
*Xmobar* instances according to how many monitors you have. This is how
I set them up:

```haskell
main = do
    -- Xmobar
    xmobarLaptop <- spawnPipe "xmobar -x 0 ~/.config/xmobar/laptop.hs"
    xmobarMonitor <- spawnPipe "xmobar -x 1 ~/.config/xmobar/monitor.hs"
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

Once that's done, you can login. But keep in mind keybindings will not work
unless you have the same programs that I use and the same configs. You can
either change keybindings or install the software I use and my config files,
check out [this section](https://github.com/antoniosarosi/dotfiles#keybindings)
for instructions.
