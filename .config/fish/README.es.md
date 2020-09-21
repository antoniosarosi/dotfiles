# Fish

![Fish](./fish.png)

***Idioma***
- Español 🇪🇸
- [English 🇺🇸](https://github.com/antoniosarosi/dotfiles/tree/master/.config/fish)

Instala *fish* y las dependencias:

```bash
sudo pacman -S fish
curl -L https://get.oh-my.fish | fish
omf install spacefish
```

Copia mis configs:

```bash
git clone https://github.com/antoniosarosi/dotfiles.git
cp -r dotfiles/.config/fish ~/.config
```

Cambia tu shell:

```bash
# Lista los shells disponibles
chsh -l
# Cambia tu shell
chsh -s /bin/fish
```
