# Rofi

![Rofi](./rofi.png)

***Idioma***
- 🇪🇸 Español
- [🇺🇸 English](https://github.com/antoniosarosi/dotfiles/tree/master/.config/rofi)

Instala *rofi* y las dependencias:

```bash
sudo pacman -S rofi papirus-icon-theme
yay -S nerd-fonts-ubuntu-mono
git clone https://github.com/davatorium/rofi-themes.git
sudo cp rofi-themes/User\ Themes/onedark.rasi /usr/share/rofi/themes
```

Borra esta línea en **/usr/share/rofi/themes/onedark.rasi**

```css
font: "Knack Nerd Font 14";
```

Copia mis configuraciones:

```bash
git clone https://github.com/antoniosarosi/dotfiles.git
cp -r dotfiles/.config/rofi ~/.config
```

Si estás usando mis configuraciones, **mod + m** lanzará
*rofi -show drun* (menu) y **mod + shift + m** lanzará *rofi -show*
(navegación de ventanas).
