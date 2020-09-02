![Neovim](./neovim.png)

***Language***
- [🇪🇸 Español](./README.es.md)
- 🇺🇸 English


To use this config, first download some dependencies:

```bash
# Vim-plug
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'

# Some runtimes are needed, install only those you don't have
sudo pacman -S nodejs npm python python-pip ruby rubygems

# Download neovim packages
pip install neovim
gem install neovim
sudo npm i -g neovim

# Some other dependencies
sudo pacman -S xsel fzf ripgrep fd the_silver_searcher prettier
yay -S universal-ctags-git
```

Now open *neovim* and execute *:PlugInstall*. Close *neovim*, and next time
you open it all my configs should be applied. This are some keybingins besides
default ones:

| Key                    | Action                                 |
| ---------------------- | -------------------------------------- |
| **jk** or **kj**       | Go to normal mode (from insert)        |
| **alt + [hjkl]**       | Resize split                           |
| **control + [hjkl]**   | Navigate splits                        |
| **control + s**        | Save                                   |
| **control + q**        | Save and quit                          |
| **tab**                | Next buffer                            |
| **shift + tab**        | Previous buffer                        |
| **control + b**        | Close buffer                           |
| **shift + <** or **>** | Indent one level or remove it (visual) |
| **shift + k** or **j** | Move selected line down or up (visual) |

***Plugin keybindings***:

| Key           | Action                                        |
| ------------- | --------------------------------------------- |
| **space + f** | Fuzzy search                                  |
| **space + /** | Comment selected line or block                |
| **space + n** | Toggle NerdTree                               |
| **space + p** | Format document with prettier                 |
| **shift + k** | Function or class documentation and arg types |
