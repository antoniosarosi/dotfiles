# Alacritty

![Alacritty](./alacritty.png)

***Idioma***
- Español 🇪🇸
- [English 🇺🇸](https://github.com/antoniosarosi/dotfiles/tree/master/.config/alacritty)

Instala *alacritty* y las dependencias:

```bash
sudo pacman -S alacritty
yay -S nerd-fonts-ubuntu-mono
```

Copia mis configuraciones:

```bash
git clone https://github.com/antoniosarosi/dotfiles.git
cp -r dotfiles/.config/alacritty ~/.config
```

Copia el fichero de configuración a otro llamado *alacritty.yml*:

```bash
cd ~/.config/alacritty
cp config.yml alacritty.yml
```

La razón por la que lo tengo hecho de esta manera es porque de otra forma Git
me avisaría de archivos modificados cada vez que cambio el tema de colores, pero
así el tema es independiente del archivo de configuración.

Uso del script automático para temas:

```bash
~/.config/alacritty/theme.py dracula
```

Solo funciona con temas disponibles en **~/.config/alacritty/themes**.
Puedes añadir esto en tu **~/.xprofile**:

```bash
export PATH=$HOME/.local/bin:$PATH
```

Lo cual te permitirá crear un enlace simbólico a ese script:

```bash
cd ~/.local/bin
ln -s ~/.config/alacritty/theme.py set-alacritty-theme

# Ahora lo puedes usar así (la próxima vez que inicies sesión)
set-alacritty-theme onedark
```
