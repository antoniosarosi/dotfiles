# Spectrwm

![Spectrwm](../../.screenshots/spectrwm.png)

***Idioma***
- 🇪🇸 Español
- [🇺🇸 English](https://github.com/antoniosarosi/dotfiles/tree/master/.config/spectrwm)

## Instalación

Instala Spectrwm y las dependencias:

```bash
sudo pacman -S spectrwm trayer upower pamixer brightnessctl pacman-contrib
yay -S nerd-fonts-ubuntu-mono
```

Clona este repositorio y copia mis configuraciones:

```bash
git clone https://github.com/antoniosarosi/dotfiles.git
cp -r dotfiles/.config/spectrwm ~/.config
```

## Autostart

Esta configuración, a diferencia de la de
[Qtile](https://github.com/antoniosarosi/dotfiles/tree/master/.config/qtile),
es bastante sencilla, Spectrwm no deja muchas posibilidades ya que se configura
con un archivo `.conf`. Primero, tenemos un script para el `autostart`, que
lanza `trayer`:

```bash
#!/bin/bash

# Spectrwm autostart script

trayer                 \
    --edge top         \
    --monitor 1        \
    --widthtype pixel  \
    --width 100        \
    --heighttype pixel \
    --height 18        \
    --align right      \
    --margin 455       \ # Ajusta este valor si es necesario
    --transparent true \
    --alpha 0          \
    --tint 0x0F101A    \
    --iconspacing 3    \
    --distance 1 &
```

## Baraction

Después tenemos un script para el *baraction*, para que funcione tienes que
instalar estas dependencias:

```bash
sudo pacman -S pacman-contrib upower brightnessctl pamixer
```

Pruébalo con [`Xephyr`](https://wiki.archlinux.org/index.php/Xephyr):

```bash
Xephyr -br -ac -noreset -screen 1280x720 :1 &
DISPLAY=:1 spectrwm
```

Si la batería no funciona (si estás en un portátil, claro),  busca esta línea en
`baraction.sh`:

```bash
bat=`upower -i /org/freedesktop/UPower/devices/battery_BAT1 |
    grep percentage |
    sed 's/ *percentage: *//g'`
```

Puede que necesites cambiar `battery_BAT1` por el valor que veas en esta salida:

```bash
upower -d
```

Una vez eso está hecho, puedes iniciar sesión. Pero recuerda que los atajos de
teclado no funcionarán a no ser que tengas todos los programas que uso yo y las
mismas configuraciones. Puedes cambiar los atajos de teclado o bien instalar el
software que uso yo, mira
[esta sección](https://github.com/antoniosarosi/dotfiles/blob/master/README.es.md#atajos-de-teclado)
para las instrucciones.

## Bar format

En `spectrwm.conf` puedes encontrar esta línea:

```ini
bar_format = +|L+@fn=2; +@fn=0;+@fg=1; +D+@fn=1;+@fg=2;+3<+W+|R+@fn=2;+A
```

Tiene una sintaxis extraña, pero básicamente, cada vez que pone `+@fn=X;` se
usa una fuente distinta, y `+@fg=X;` significa un color de fuente distinto.
Así es como se definen los colores y fuentes:

```ini
# ...
bar_font = UbuntuMono Nerd Font:size=16, UbuntuMono Nerd Font:size=10, UbuntuMono Nerd Font:size=13
# ...
bar_font_color[1] = rgb:a6/ac/cd, rgb:e4/6a/6a, rgb:4c/56/6a
# ...
```

Para documentación específica:

```bash
man spectrwm
```

Lee `spectrwm.conf` y `~/.config/spectrwm/baraction.sh` para entender el
resto de la configuración.
