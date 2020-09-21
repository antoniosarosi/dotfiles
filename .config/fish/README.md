# Fish

![Fish](./fish.png)

***Language***
- [🇪🇸 Español](./README.es.md)
- 🇺🇸 English


Install *fish* and dependencies:

```bash
sudo pacman -S fish
curl -L https://get.oh-my.fish | fish
omf install spacefish
```

Copy my configs:

```bash
git clone https://github.com/antoniosarosi/dotfiles.git
cp -r dotfiles/.config/fish ~/.config
```

Change your shell:

```bash
# List available shells
chsh -l
# Change shell
chsh -s /bin/fish
```
