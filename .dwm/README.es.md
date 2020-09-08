![Dwm](../.screenshots/dwm.png)

***Idioma***
- 🇪🇸 Español
- [🇺🇸 English](https://github.com/antoniosarosi/dotfiles/tree/master/.dwm)

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
- [pertag](https://dwm.suckless.org/patches/pertag/)
- [cyclelayouts](https://dwm.suckless.org/patches/cyclelayouts/dwm-cyclelayouts-20180524-6.2.diff)

Para instalarlo en tu sistema, primero necesitas unas dependencias:

```bash
yay -S nerd-fonts-ubuntu-mono
```

Siempre uso esa fuente para iconos. También necesitarás mi
**[dwmblocks](https://github.com/antoniosarosi/dotfiles/tree/master/.config/dwmblocks)**
y scripts situados en
**[~/.local/bin](https://github.com/antoniosarosi/dotfiles/tree/master/.local/bin)**.

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

# Dependencias de los scripts
sudo pacman -S pacman-contrib brightnessctl pamixer upower
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

Para el *autostart* abre **~/.dwm/autostart.sh**.
Pruébalo con **[Xephyr](https://wiki.archlinux.org/index.php/Xephyr)**:

```bash
Xephyr -br -ac -noreset -screen 1280x720 :1 &
DISPLAY=:1 dwm
```

Para añadir o quitar iconos en la barra, abre **~/.config/dwmblocks/config.h**
y modifica estas líneas:

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

Después, recompila *dwmblocks* y vuelve a lanzar *dwm* con
**mod + control + r**.

```bash
cd ~/.config/dwmblocks
sudo make clean install
```

Una vez eso está hecho, puedes iniciar sesión. Pero recuerda que los atajos de
teclado no funcionarán a no ser que tengas todos los programas que uso yo y las
mismas configuraciones. Puedes cambiar los atajos de teclado o bien instalar el
software que uso yo, mira
[esta sección](https://github.com/antoniosarosi/dotfiles/blob/master/README.es.md#atajos-de-teclado)
para las instrucciones.
