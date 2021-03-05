# Qtile

![Qtile](../../.screenshots/qtile.png)

***Idioma***
- 🇪🇸 Español
- [🇺🇸 English](https://github.com/antoniosarosi/dotfiles/tree/master/.config/qtile)

## Instalación (Arch)

Instala Qtile y las dependencias:

```bash
sudo pacman -S qtile pacman-contrib
yay -S nerd-fonts-ubuntu-mono
pip install psutil
```

Clona este repositorio y copia mis configuraciones:

```bash
git clone https://github.com/antoniosarosi/dotfiles.git
cp -r dotfiles/.config/qtile ~/.config
```

Pruébalo con **[Xephyr](https://wiki.archlinux.org/index.php/Xephyr)**:

```bash
Xephyr -br -ac -noreset -screen 1280x720 :1 &
DISPLAY=:1 qtile
```

Si el icono de la red no funciona, abre  ```./settings/widgets.py``` y busca
esta línea, debería estar dentro de una lista llamada *primary_widgets*:

```python
# Cambia el argumento "interface", usa ip address para saber cuál poner
 widget.Net(**base(bg='color3'), interface='wlp2s0'),
```

Una vez eso está hecho, puedes iniciar sesión. Pero recuerda que los atajos de
teclado no funcionarán a no ser que tengas todos los programas que uso yo y las
mismas configuraciones. Puedes cambiar los atajos de teclado o bien instalar el
software que uso yo, mira
[esta sección](https://github.com/antoniosarosi/dotfiles/blob/master/README.es.md#atajos-de-teclado)
para las instrucciones.

## Estructura

En el archivo ```config.py``` que es donde la mayoría suele poner toda su
configuración, yo solo tengo el *autostart* y algunas variables como
*cursor_warp*.

```python
@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostart.sh')])
```

Para cambiar lo que se lanza en el *autostart* abre el archivo 
```./autostart.sh```.

```bash
#!/bin/sh

# systray battery icon
cbatticon -u 5 &
# systray volume
volumeicon &
```

Si quieres añadir o quitar atajos de teclado, abre ```./settings/keys.py```.
Para añadir o quitar espacios de trabajos, debes modificar
```./settings/groups.py```. Finalmente, si quieres añadir nuevos *layouts*,
abre ```./settings/layouts.py```, el resto de archivos no hace falta tocarlos.

## Temas

Para establecer un tema, mira los que hay disponibles en ```./themes```, y
coloca su nombre en un archivo llamado ```./config.json```:

```json
{
    "theme": "material-ocean"
}
```
