# Dotfiles & Configs

![Qtile](.screenshots/qtile.png)

***Language***
- [🇪🇸 Español](./README.es.md)
- 🇺🇸 English

***Quick Links***
- *Window manager configs*
  - [Qtile](https://github.com/antoniosarosi/dotfiles/tree/master/.config/qtile)
  - [Spectrwm](https://github.com/antoniosarosi/dotfiles/tree/master/.config/spectrwm)
  - [Openbox](https://github.com/antoniosarosi/dotfiles/tree/master/.config/openbox)
  - [Xmonad](https://github.com/antoniosarosi/dotfiles/tree/master/.xmonad)
  - [Dwm](https://github.com/antoniosarosi/dotfiles/tree/master/.dwm)
- [Gallery (see how my configs look)](#gallery)
- [Common keybindings for my configs](#keybindings)
- [Software I use](#software)

# Table of Contents

- [Overview](#overview)
- [Arch installation](#arch-installation)
- [Login and window manager](#login-and-window-manager)
- [Basic qtile configuration](#basic-qtile-configuration)
- [Basic system utilities](#basic-system-utilities)
  - [Wallpaper](#wallpaper)
  - [Fonts](#fonts)
  - [Audio](#audio)
  - [Monitors](#monitors)
  - [Storage](#storage)
  - [Network](#network)
  - [Systray](#systray)
  - [Notifications](#notifications)
  - [Xprofile](#xprofile)
- [Further configuration and tools](#further-configuration-and-tools)
  - [AUR helper](#aur-helper)
  - [Media Transfer Protocol](#media-transfer-protocol)
  - [File Manager](#file-manager)
  - [Trash](#trash)
  - [GTK Theming](#gtk-theming)
  - [Lightdm theming](#lightdm-theming)
  - [Multimedia](#multimedia)
    - [Images](#images)
    - [Video and audio](#video-and-audio)
  - [Start Hacking](#start-hacking)
- [Gallery](#gallery)
  - [Qtile](#qtile)
  - [Spectrwm](#spectrwm)
  - [Openbox](#openbox)
  - [Xmonad](#xmonad)
  - [Dwm](#dwm)
- [Keybindings](#keybindings)
  - [Windows](#windows)
  - [Apps](#apps)
- [Software](#software)
  - [Basic utilities](#basic-utilities)
  - [Fonts, theming and GTK](#fonts-theming-and-gtk)
  - [Apps](#apps-1)

# Overview

This guide will walk you through the process of building a desktop environment
starting with a fresh Arch based installation. I will assume that you are
comfortable with Linux based operating systems and command line interfaces.
Because you are reading this, I will also assume that you've looked through some
"tiling window manager" videos on Youtube, because that's where the rabbit hole
starts. You can pick any window managers you want, but I'm going to use Qtile
as a first tiling window manager because that's what I started with. This is
basically a description of how I made my desktop environment from scratch.

# Arch installation

The starting point of this guide is right after a complete clean Arch based
distro installation. The
**[Arch Wiki](https://wiki.archlinux.org/index.php/Installation_guide)**
doesn't tell you what to do after setting the root password, it suggests installing
a bootloader, but before that I would make sure to have working internet:

```bash
pacman -S networkmanager
systemctl enable NetworkManager
```

Now you can install a bootloader and test it "safely", this is how to do it on
modern hardware,
[assuming you've mounted the efi partition on /boot](https://wiki.archlinux.org/index.php/Installation_guide#Example_layouts):

```bash
pacman -S grub efibootmgr os-prober
grub-install --target=x86_64-efi --efi-directory=/boot
os-prober
grub-mkconfig -o /boot/grub/grub.cfg
```

Now you can create your user:

```bash
useradd -m username
passwd username
usermod -aG wheel,video,audio,storage username
```

In order to have root privileges we need sudo:

```bash
pacman -S sudo
```

Edit **/etc/sudoers** with nano or vim by uncommenting this line:

```bash
## Uncomment to allow members of group wheel to execute any command
# %wheel ALL=(ALL) ALL
```

Now you can reboot:

```bash
# Exit out of ISO image, unmount it and remove it
exit
umount -R /mnt
reboot
```

After logging in, your internet should be working just fine, but that's only if
your computer is plugged in. If you're on a laptop with no Ethernet ports, you
might have used **[iwctl](https://wiki.archlinux.org/index.php/Iwd#iwctl)**
during installation, but that program is not available anymore unless you have
installed it explicitly. However, we've installed
**[NetworkManager](https://wiki.archlinux.org/index.php/NetworkManager)**,
so no problem, this is how you connect to a wireless LAN with this software:

```bash
# List all available networks
nmcli device wifi list
# Connect to your network
nmcli device wifi connect YOUR_SSID password YOUR_PASSWORD
```

Check [this page](https://wiki.archlinux.org/index.php/NetworkManager#nmcli_examples)
for other options provided by *nmcli*. The last thing we need to do before
thinking about desktop environments is installing **[Xorg](https://wiki.archlinux.org/index.php/Xorg)**:

```bash
sudo pacman -S xorg
```

# Login and window manager

First, we need to be able to login and open some programs like a browser and a
terminal, so we'll start by installing **[lighdm](https://wiki.archlinux.org/index.php/LightDM)**
and **[qtile](https://wiki.archlinux.org/index.php/Qtile)**. Lightdm will not
work unless we install a **[greeter](https://wiki.archlinux.org/index.php/LightDM#Greeter)**.
We also need
**[xterm](https://wiki.archlinux.org/index.php/Xterm)** because that's the
terminal emulator qtile will open by default, until we change the config file.
Then, a text editor is necessary for editing config files, you can use
**[vscode](https://wiki.archlinux.org/index.php/Visual_Studio_Code)** or jump
straight into **[neovim](https://wiki.archlinux.org/index.php/Neovim)** if you
have previous experience, otherwise I wouldn't suggest it. Last but not least,
we need a browser.

```bash
sudo pacman -S lightdm lightdm-gtk-greeter qtile xterm code firefox
```

Enable *lightdm* service and restart your computer, you should be able to log into
Qtile through *lightdm*.

```bash
sudo systemctl enable lightdm
reboot
```

# Basic qtile configuration

Now that you're in Qtile, you should know some of the default keybindings.

| Key                  | Action                     |
| -------------------- | -------------------------- |
| **mod + return**     | launch xterm               |
| **mod + k**          | next window                |
| **mod + j**          | previous window            |
| **mod + w**          | kill window                |
| **mod + [asdfuiop]** | go to workspace [asdfuiop] |
| **mod + ctrl + r**   | restart qtile              |
| **mod + ctrl + q**   | logout                     |

Before doing anything else, if you don't have a US keyboard, you should
change it using *setxkbmap*. To open xterm use **mod + return**. For example to
change your layout to spanish:

```bash
setxkbmap es
```

Note that this change is not permanent, if you reboot you have to type that
command again. See [this section](#xprofile) for making it permanent, or
follow the natural order of this guide if you have enough time.

There is no menu by default, you have to launch programs through xterm. At this
point, you can pick your terminal emulator of choice and install a program
launcher.

```bash
# Install another terminal emulator if you want
sudo pacman -S alacritty
```

Now open the config file:

```bash
code ~/.config/qtile/config.py
```

At the beginning, after imports, you should find an array called *keys*,
and it contains the following line:

```python
Key([mod], "Return", lazy.spawn("xterm")),
```

Change that line to launch your terminal emulator:

```python
Key([mod], "Return", lazy.spawn("alacritty")),
```

Install a program launcher like
**[dmenu](https://wiki.archlinux.org/index.php/Dmenu)**
or **[rofi](https://wiki.archlinux.org/index.php/Rofi)**:

```bash
sudo pacman -S rofi
```

Then add keybindings for that program:

```python
Key([mod], "m", lazy.spawn("rofi -show run")),
Key([mod, 'shift'], "m", lazy.spawn("rofi -show")),
```

Now restart Qtile with **mod + control + r**. You should be able to open your
menu and terminal emulator with keybindings. If you picked rofi, you can
change its theme like so:

```bash
sudo pacman -S which
rofi-theme-selector
```

That's it for Qtile, now you can start hacking on it and make it your own.
Checkout my custom Qtile config
[here](https://github.com/antoniosarosi/dotfiles/tree/master/.config/qtile).
But before that I would recommend configuring basic utilities like audio,
battery, mounting drives, etc.

# Basic system utilities

In this section we will cover some software that almost everybody needs on their
system. Keep in mind though that the changes we are going to make
will not be permanent. [This subsection](#xprofile) describes how to accomplish
that.

## Wallpaper

First things first, your screen looks empty and black, so you might want to have
a wallpaper not to feel so depressed. You can open *firefox* through *rofi*
using **mod + m** and download one. Then install
**[feh](https://wiki.archlinux.org/index.php/Feh)** or
**[nitrogen](https://wiki.archlinux.org/index.php/Nitrogen)**
and and set your wallpaper:

```bash
sudo pacman -S feh
feh --bg-scale path/to/wallpaper
```

## Fonts

Fonts in Arch Linux are basically a meme, before you run into any problems
you can just use the simple approach of installing these packages:

```bash
sudo pacman -S ttf-dejavu ttf-liberation noto-fonts
```

To list all available fonts:

```bash
fc-list
```

## Audio

There is no audio at this point, we need
**[pulseaudio](https://wiki.archlinux.org/index.php/PulseAudio)**.
I suggest also installing a graphical program to control audio like
**[pavucontrol](https://www.archlinux.org/packages/extra/x86_64/pavucontrol/)**,
because we don't have keybindings for that yet:

```bash
sudo pacman -S pulseaudio pavucontrol
```

On Arch,
[pulseaudio is enabled by default](https://wiki.archlinux.org/index.php/PulseAudio#Running),
but you might need to reboot in order for it to actually start. After rebooting,
you can open *pavucontrol* through *rofi*, unmute the audio, and you should be
just fine.

Now you can set up keybindings for *pulseaudio*, open Qtile's config.py and add
these keys:

```python
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
```

For a better CLI experience though, I recommend using
**[pamixer](https://www.archlinux.org/packages/community/x86_64/pamixer/)**:

```bash
sudo pacman -S pamixer
```

Now you can turn your keybindings into:

```python
# Volume
Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
```

Restart Qtile with **mod + control + r** and your keybindings should work. If
you're on a laptop, you might also want to control the brightness of your screen,
and for that I recommend
**[brightnessctl](https://www.archlinux.org/packages/community/x86_64/brightnessctl/)**:

```bash
sudo pacman -S brightnessctl
```

You can add these keybindings and restart Qtile after:

```python
# Brightness
Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
```

## Monitors

If you have a multi-monitor system, you surely want to use all your screens.
Here's how **[xrandr](https://wiki.archlinux.org/index.php/Xrandr)** CLI works:

```bash
# List all available outputs and resolutions
xrandr
# Common setup for a laptop and a monitor
xrandr --output eDP-1 --primary --mode 1920x1080 --pos 0x1080 --output HDMI-1 --mode 1920x1080 --pos 0x0
```

We need to specify the position for each output, otherwise it will default to
0x0, and all your outputs will be overlapped. Now if you don't want to calculate pixels
and stuff you need a GUI like
**[arandr](https://www.archlinux.org/packages/community/any/arandr/)**:

```bash
sudo pacman -S arandr
```

Open it with *rofi*, arrange your screens however you want, and then you can
save that layout, which will basically give you a shell script with the exact
*xrandr* command that you need. Save that script, but don't click "apply" just
yet.

For a multi-monitor system, it's recommended to create an instance of a
*Screen* object for each monitor in your Qtile config.

You'll find an array called *screens* which contains only one object
initialized with a bar at the bottom. Inside that bar you can see the default
widgets that come with it.

Add as many screens as you have and copy-paste all widgets, later you can
customize them. Now you can go back to arandr, click *apply*, and then restart
Qtile.

Now your multi-monitor system should work.

## Storage

Another basic utility you might need is automounting external hard drives or
USBs. For that I use **[udisks](https://wiki.archlinux.org/index.php/Udisks)**
and **[udiskie](https://www.archlinux.org/packages/community/any/udiskie/)**.
*udisks* is a dependency of *udiskie*, so we only need to install the last one.
Install also **[ntfs-3g](https://wiki.archlinux.org/index.php/NTFS-3G)**
package to read and write NTFS formatted drives:

```bash
sudo pacman -S udiskie ntfs-3g
```

## Network

We have configured the network through *nmcli*, but a graphical frontend is
more friendly. I use
**[nm-applet](https://wiki.archlinux.org/index.php/NetworkManager#nm-applet)**:

```bash
sudo pacman -S network-manager-applet
```

## Systray

By default, you have a system tray in Qtile, but there's nothing running in it.
You can launch the programs we've just installed like so:

```bash
udiskie -t &
nm-applet &
```

Now you should see icons that you can click to configure drives and networking.
Optionally, you can install tray icons for volume and battery:

```bash
sudo pacman -S volumeicon cbatticon
volumeicon &
cbatticon &
```

## Notifications

I like having desktop notifications as well, for that you need to install
[**libnotify**](https://wiki.archlinux.org/index.php/Desktop_notifications#Libnotify)
and [**notification-daemon**](https://www.archlinux.org/packages/community/x86_64/notification-daemon/):

```bash
sudo pacman -S libnotify notification-daemon
```

For a tiling window manager,
[this is how you can get notifications](https://wiki.archlinux.org/index.php/Desktop_notifications#Standalone):

```bash
# Create this file with nano or vim
sudo nano /usr/share/dbus-1/services/org.freedesktop.Notifications.service
# Paste these lines
[D-BUS Service]
Name=org.freedesktop.Notifications
Exec=/usr/lib/notification-daemon-1.0/notification-daemon
```

Test it like so:

```bash
notification-send "Hello World"
```

## Xprofile

As I have mentioned before, all these changes are not permanent. In order to
make them permanent, we need a couple things. First, install
**[xinit](https://wiki.archlinux.org/index.php/Xinit)**:


```bash
sudo pacman -S xorg-xinit
```

Now you can use *~/.xprofile* to run programs before your window manager starts:

```bash
touch ~/.xprofile
```

For example, if you place this in *~.xprofile*:

```bash
xrandr --output eDP-1 --primary --mode 1920x1080 --pos 0x1080 --output HDMI-1 --mode 1920x1080 --pos 0x0 &
setxkbmap es &
nm-applet &
udiskie -t &
volumeicon &
cbatticon &
```

Every time you login you will have all systray utilities, your keyboard layout
and monitors set.

# Further configuration and tools

## AUR helper

Now that you have some software that allows you tu use your computer without
losing your patience, it's time to do more interesting stuff. First, install an
**[AUR helper](https://wiki.archlinux.org/index.php/AUR_helpers)**, I use
**[yay](https://github.com/Jguer/yay)**:

```bash
sudo pacman -S base-devel git
cd /opt/
sudo git clone https://aur.archlinux.org/yay-git.git
sudo chown -R username:username yay-git/
cd yay-git
makepkg -si
```

With an *Arch User Repository helper*, you can basically install
any piece of software on this planet that was meant to run on Linux.

## Media Transfer Protocol

If you want to connect your phone to your computer using a USB port, you'll
need MTP implementation and some CLI to use it, like
[this one](https://aur.archlinux.org/packages/simple-mtpfs/):

```bash
sudo pacman -S libmtp
yay -S simple-mtpfs

# List connected devices
simple-mtpfs -l
# Mount first device in the previous list
simple-mtpfs --device 1 /mount/point
```

## File Manager

We've done all files stuff through a terminal up to this point, but you can
install graphical or terminal based file managers.
For a graphical one, I suggest
**[thunar](https://wiki.archlinux.org/index.php/Thunar)**
and for a terminal based one,
**[ranger](https://wiki.archlinux.org/index.php/Ranger)**, although this one
is very vim-like, only use it if you know how to move in vim.

```bash
sudo pacman -S thunar ranger
```

## Trash

If you don't want to *rm* all the time and potentially lose files, you need a
trashing system. Luckily, that's pretty easy to do, using
[some of these tools](https://wiki.archlinux.org/index.php/Trash_management#Trash_creation)
such as **[glib2](https://www.archlinux.org/packages/core/x86_64/glib2/)**,
and for GUIs like *thunar* you need **[gvfs](https://www.archlinux.org/packages/extra/x86_64/gvfs/)**:

```bash
sudo pacman -S glib2 gvfs
# CLI usage
gio trash path/to/file
# Empty trash
gio trash --empty
```

With *thunar* you can open the trash clicking on the left panel, but on the command
line you can use:

```bash
ls ~/.local/share/Trash/files
```

## GTK Theming

The moment you have been wating for has arrived, you are finally going to
install a dark theme. I use *Material Black Colors*, so go grab a flavor
[here](https://www.gnome-look.org/p/1316887/) and the matching icons
[here](https://www.pling.com/p/1333360/).

I suggest starting with
*Material-Black-Blueberry* and *Material-Black-Blueberry-Suru*. You can find
other GTK themes [on this page](https://www.gnome-look.org/browse/cat/135/).
Once you have your theme folders downloaded, this is what you do:

```bash
# Assuming you have downloaded Material-Black-Blueberry
cd Downloads/
sudo pacman -S unzip
unzip Material-Black-Blueberry.zip
unzip Material-Black-Blueberry-Suru.zip
rm Material-Black*.zip

# Make your themes available
sudo mv Material-Black-Blueberry /usr/share/themes
sudo mv Material-Black-Blueberry-Suru /usr/share/icons
```

Now edit **~/.gtkrc-2.0** and **~/.config/gtk-3.0/settings.ini** by adding
these lines:

```ini
# ~/.gtkrc-2.0
gtk-theme-name = "Material-Black-Blueberry"
gtk-icon-theme-name = "Material-Black-Blueberry-Suru"

# ~/.config/gtk-3.0/settings.ini
gtk-theme-name = Material-Black-Blueberry
gtk-icon-theme-name = Material-Black-Blueberry-Suru
```

Next time you log in, these changes will be visible. You can also install a
different cursor theme, for that you need
**[xcb-util-cursor](https://www.archlinux.org/packages/extra/x86_64/xcb-util-cursor/)**.
The theme I use is
[Breeze](https://www.gnome-look.org/p/999927/), download it and then:

```bash
sudo pacman -S xcb-util-cursor
cd Downloads/
tar -xf Breeze.tar.gz
sudo mv Breeze /usr/share/icons
```

Edit **/usr/share/icons/default/index.theme** by adding this:

```ini
[Icon Theme]
Inherits = Breeze
```

Now, again, edit **~/.gtkrc-2.0** and **~/.config/gtk-3.0/settings.ini**:

```ini
# ~/.gtkrc-2.0
gtk-cursor-theme-name = "Breeze"

# ~/.config/gtk-3.0/settings.ini
gtk-cursor-theme-name = Breeze
```

Make sure not to mistype the names of your themes and icons, they should
match the names of the directories where they are located, the ones you can
see in this output:

```bash
ls /usr/share/themes
ls /usr/share/icons
```

Remember that you will only see the new theme if you log in again.
There are also graphical frontends for changing themes, I just prefer the
traditional way of editing files though, but you can use
**[lxappearance](https://www.archlinux.org/packages/community/x86_64/lxappearance/)**,
which is a desktop environment independent GUI for this task, and it lets you
preview themes.

```bash
sudo pacman -S lxappearance
```

Finally, if you want tranparency and fancy looking things, install a compositor:

```bash
sudo pacman -S picom
# Run it like so, place it in ~/.xrofile
picom &
```

## Lightdm theming

We can also change the theme of *lightdm* and make it look cooler, because why
not? We need another greeter, and some theme, namely
**[lightdm-webkit2-greeter](https://www.archlinux.org/packages/community/x86_64/lightdm-webkit2-greeter/)**
and  **[lightdm-webkit-theme-aether](https://aur.archlinux.org/packages/lightdm-webkit-theme-aether/)**:

```bash
sudo pacman -S lightdm-webkit2-greeter
yay -S lightdm-webkit-theme-aether
```

These are the configs you need to make:

```ini
# /etc/lightdm/lightdm.conf
[Seat:*]
# ...
# Uncomment this line and set this value
greeter-session = lightdm-webkit2-greeter
# ...

# /etc/lightdm/lightdm-webkit2-greeter.conf
[greeter]
# ...
webkit_theme = lightdm-webkit-theme-aether
```

Ready to go.

## Multimedia

There are dozens of programs for multimedia stuff, check
[this page](https://wiki.archlinux.org/index.php/List_of_applications/Multimedia).

### Images

For image previews, one of the best that I could find is
[geeqie](https://www.archlinux.org/packages/extra/x86_64/geeqie/):

```bash
sudo pacman -S geeqie
```

### Video and audio

No doubt
[vlc](https://wiki.archlinux.org/index.php/VLC_media_player_(Espa%C3%B1ol))
is exactly what you need:

```bash
sudo pacman -S vlc
```

You might want a dark theme though.

```bash
yay -S vlc-arc-dark-git
```

Open *vlc*, tools, preferences, "use custom skin", and choose this file:
**/usr/share/vlc/skins2/Arc-Dark-Fixed-Size.vlt**

Then save changes, and you can use *vlc* for audio and video playing.

## Start Hacking

With all you've done so far, you got all the tools to start playing with configs
and make your desktop environment, well, yours. What I recommend is hacking
on Qtile to adding keybindings for common programs like *firefox*,
a text editor, file manager, etc.

Once you feel comfortable with Qtile, you can install other
tiling window managers, and you will have more sessions available when logging
in through *lightdm*.

Here you have a list of all my window manager configs,
which are located in this repository and have their own documentation:

- [Qtile](https://github.com/antoniosarosi/dotfiles/tree/master/.config/qtile)
- [Spectrwm](https://github.com/antoniosarosi/dotfiles/tree/master/.config/spectrwm)
- [Openbox](https://github.com/antoniosarosi/dotfiles/tree/master/.config/openbox)
- [Xmonad](https://github.com/antoniosarosi/dotfiles/tree/master/.xmonad)
- [Dwm](https://github.com/antoniosarosi/dotfiles/tree/master/.dwm)

# Gallery

## [Qtile](https://github.com/antoniosarosi/dotfiles/tree/master/.config/qtile)
![Qtile](.screenshots/qtile.png)

## [Spectrwm](https://github.com/antoniosarosi/dotfiles/tree/master/.config/spectrwm)
![Spectrwm](.screenshots/spectrwm.png)

## [Openbox](https://github.com/antoniosarosi/dotfiles/tree/master/.config/openbox)
![Spectrwm](.screenshots/openbox.png)

## [Xmonad](https://github.com/antoniosarosi/dotfiles/tree/master/.xmonad)
![Spectrwm](.screenshots/xmonad.png)

## [Dwm](https://github.com/antoniosarosi/dotfiles/tree/master/.dwm)
![Spectrwm](.screenshots/dwm.png)

# Keybindings

These are common keybindings to all my window managers.

## Windows

| Key                     | Action                           |
| ----------------------- | -------------------------------- |
| **mod + j**             | next window (down)               |
| **mod + k**             | next window (up)                 |
| **mod + shift + h**     | decrease master                  |
| **mod + shift + l**     | increase master                  |
| **mod + shift + j**     | move window down                 |
| **mod + shift + k**     | move window up                   |
| **mod + shift + f**     | toggle floating                  |
| **mod + tab**           | change layout                    |
| **mod + [1-9]**         | Switch to workspace N (1-9)      |
| **mod + shift + [1-9]** | Send Window to workspace N (1-9) |
| **mod + period**        | Focus next monitor               |
| **mod + comma**         | Focus previous monitor           |
| **mod + w**             | kill window                      |
| **mod + ctrl + r**      | restart wm                       |
| **mod + ctrl + q**      | quit                             |

The following keybindings will only work if you install all programs needed:

```bash
sudo pacman -S rofi thunar firefox alacritty redshift scrot
```

To set up *rofi*,
[check this README](https://github.com/antoniosarosi/dotfiles/tree/master/.config/rofi),
and for *alacritty*, [this one](https://github.com/antoniosarosi/dotfiles/tree/master/.config/alacritty).


## Apps

| Key                 | Action                        |
| ------------------- | ----------------------------- |
| **mod + m**         | launch rofi                   |
| **mod + shift + m** | window nav (rofi)             |
| **mod + b**         | launch browser (firefox)      |
| **mod + e**         | launch file explorer (thunar) |
| **mod + return**    | launch terminal (alacritty)   |
| **mod + r**         | redshift                      |
| **mod + shift + r** | stop redshift                 |
| **mod + s**         | screenshot (scrot)            |

# Software

## Basic utilities

| Software                                                                                            | Utility                          |
| --------------------------------------------------------------------------------------------------- | -------------------------------- |
| **[networkmanager](https://wiki.archlinux.org/index.php/NetworkManager)**                           | Self explanatory                 |
| **[network-manager-applet](https://wiki.archlinux.org/index.php/NetworkManager#nm-applet)**         | *NetworkManager* systray         |
| **[pulseaudio](https://wiki.archlinux.org/index.php/PulseAudio)**                                   | Self explanatory                 |
| **[pavucontrol](https://www.archlinux.org/packages/extra/x86_64/pavucontrol/)**                     | *pulseaudio* GUI                 |
| **[pamixer](https://www.archlinux.org/packages/community/x86_64/pamixer/)**                         | *pulseaudio* CLI                 |
| **[brightnessctl](https://www.archlinux.org/packages/community/x86_64/brightnessctl/)**             | Laptop screen brightness         |
| **[xinit](https://wiki.archlinux.org/index.php/Xinit)**                                             | Launch programs before wm starts |
| **[libnotify](https://wiki.archlinux.org/index.php/Desktop_notifications)**                         | Desktop notifications            |
| **[notification-daemon](https://www.archlinux.org/packages/community/x86_64/notification-daemon/)** | Self explanatory                 |
| **[udiskie](https://www.archlinux.org/packages/community/any/udiskie/)**                            | Automounter                      |
| **[ntfs-3g](https://wiki.archlinux.org/index.php/NTFS-3G)**                                         | NTFS read & write                |
| **[arandr](https://www.archlinux.org/packages/community/any/arandr/)**                              | GUI for *xrandr*                 |
| **[cbatticon](https://www.archlinux.org/packages/community/x86_64/cbatticon/)**                     | Battery systray                  |
| **[volumeicon](https://www.archlinux.org/packages/community/x86_64/volumeicon/)**                   | Volume systray                   |
| **[glib2](https://www.archlinux.org/packages/core/x86_64/glib2/)**                                  | Trash                            |
| **[gvfs](https://www.archlinux.org/packages/extra/x86_64/gvfs/)**                                   | Trash for GUIs                   |

## Fonts, theming and GTK

| Software                                                                               | Utility                    |
| -------------------------------------------------------------------------------------- | -------------------------- |
| **[Picom](https://wiki.archlinux.org/index.php/Picom)**                                | Compositor for Xorg        |
| **[UbuntuMono Nerd Font](https://aur.archlinux.org/packages/nerd-fonts-ubuntu-mono/)** | Nerd Font for icons        |
| **[Material Black](https://www.gnome-look.org/p/1316887/)**                            | GTK theme and icons        |
| **[lxappearance](https://www.archlinux.org/packages/community/x86_64/lxappearance/)**  | GUI for changing themes    |
| **[nitrogen](https://wiki.archlinux.org/index.php/Nitrogen)**                          | GUI for setting wallpapers |
| **[feh](https://wiki.archlinux.org/index.php/Feh)**                                    | CLI for setting wallpapers |

## Apps

| Software                                                              | Utility                  |
| --------------------------------------------------------------------- | ------------------------ |
| **[alacritty](https://wiki.archlinux.org/index.php/Alacritty)**       | Terminal emulator        |
| **[thunar](https://wiki.archlinux.org/index.php/Thunar)**             | Graphical file explorer  |
| **[ranger](https://wiki.archlinux.org/index.php/Ranger)**             | Terminal based explorer  |
| **[neovim](https://wiki.archlinux.org/index.php/Neovim)**             | Terminal based editor    |
| **[rofi](https://wiki.archlinux.org/index.php/Rofi)**                 | Menu and window switcher |
| **[scrot](https://wiki.archlinux.org/index.php/Screen_capture)**      | Screenshot               |
| **[redshift](https://wiki.archlinux.org/index.php/Redshift)**         | Take care of your eyes   |
| **[trayer](https://www.archlinux.org/packages/extra/x86_64/trayer/)** | Systray                  |
