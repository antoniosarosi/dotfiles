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
