Dependencies:

```bash
sudo pacman -S papirus-icons
git clone https://github.com/davatorium/rofi-themes.git
sudo cp rofi-themes/User\ Themes/onedark.rasi /usr/share/rofi/themes
```

Delete this line in **/usr/share/rofi/themes/onedark.rasi**

```css
font: "Knack Nerd Font 14";
```

If you are using my window manager configs, **mod + m** will launch
*rofi -show drun* and **mod + shift + m** will launch *rofi -show*.
