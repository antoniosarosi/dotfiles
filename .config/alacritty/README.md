# Alacritty

![Alacritty](./alacritty.png)

***Language***
- [🇪🇸 Español](./README.es.md)
- 🇺🇸 English

Install *alacritty* and dependencies:

```bash
sudo pacman -S alacritty
yay -S nerd-fonts-ubuntu-mono
```

Copy my configs:

```bash
git clone https://github.com/antoniosarosi/dotfiles.git
cp -r dotfiles/.config/alacritty ~/.config
```

Now, copy the config file and name it *alacritty.yml*:

```bash
cd ~/.config/alacritty
cp config.yml alacritty.yml
```

The reason I have it set like this is because I don't want Git telling me about
modified files every time I change my theme, this way the theme is independent
of the configuration.

Theme script usage:

```bash
~/.config/alacritty/theme.py dracula
```

It will only work with themes available in **~/.config/alacritty/themes**.
You can also add this to your **~/.xprofile**:

```bash
export PATH=$HOME/.local/bin:$PATH
```

Which will allow you to create a soft link for that script:

```bash
cd ~/.local/bin
ln -s ~/.config/alacritty/theme.py set-alacritty-theme

# Now you can use it like so (next time you login again)
set-alacritty-theme onedark
```
