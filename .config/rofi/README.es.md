# Rofi

![Rofi](./rofi.png)

***Idioma***
- Español 🇪🇸
- English [🇺🇸](https://github.com/antoniosarosi/dotfiles/tree/master/.config/rofi)

Dependencias:

```bash
sudo pacman -S papirus-icon-theme
yay -S nerd-fonts-ubuntu-mono
git clone https://github.com/davatorium/rofi-themes.git
sudo cp rofi-themes/User\ Themes/onedark.rasi /usr/share/rofi/themes
```

Borra esta línea en **/usr/share/rofi/themes/onedark.rasi**

```css
font: "Knack Nerd Font 14";
```

Si estás usando mis configuraciones, **mod + m** lanzará
*rofi -show drun* (menu) y **mod + shift + m** lanzará *rofi -show*
(navegación de ventanas).
