![Dwm](../.screenshots/dwm.png)

Idioma
🇪🇸
[🇺🇸](https://github.com/antoniosarosi/dotfiles/tree/master/.dwm)

Mi versión personalizada de **[dwm](https://dwm.suckless.org/)**.

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
- [cyclelayouts](https://dwm.suckless.org/patches/cyclelayouts/dwm-cyclelayouts-20180524-6.2.diff)

Para instalarlo en tu sistema, primer necesitas una dependencias:

```bash
sudo pacman -S pacman-contrib
yay -S nerd-fonts-ubuntu-mono
```

Siempre uso esa fuente para iconos. *pacman-contrib* sirve para comprobar
actualizaciones. También necesitarás mi
**[dwmblocks](https://github.com/antoniosarosi/dotfiles/tree/master/.config/dwmblocks)**
y scripts situados en
**[~/.local/bin](https://github.com/antoniosarosi/dotfiles/tree/master/.local/bin)**.

```bash
git clone https://github.com/antoniosarosi/dotfiles.git
cp -r dotfiles/.dwm ~
cp -r dotfiles/.config/dwmblocks ~/.config/
cp dotfiles/.local/bin/battery ~/.local/bin/
cp dotfiles/.local/bin/brightness ~/.local/bin/
cp dotfiles/.local/bin/volume ~/.local/bin/
```

Escribe esto en tu **~/.xprofile**:

```bash
export PATH=$HOME/.local/bin:$PATH
```

Compila *dwm* y *dwmblocks* y crea una nueva *xsession*:

```bash
cd ~/.dwm
sudo make clean install
cd ~/.config/dwmblocks/
sudo make clean install
sudo cp ~/.dwm/dwm.desktop /usr/share/xsessions
```

Testealo con **[Xephyr](https://wiki.archlinux.org/index.php/Xephyr)**:

```bash
Xephyr -br -ac -noreset -screen 1280x720 :1 &
DISPLAY=:1 dwm
```

Una vez eso está hecho, puedes iniciar sesión. Pero recuerda que los atajos de
teclado no funcionarán a no ser que tengas todos los programas que uso yo y las
mismas configuraciones. Puedes cambiar los atajos de teclado o bien instalar el
software que uso yo, mira
[esta sección](https://github.com/antoniosarosi/dotfiles#keybindings)
para las instrucciones.
