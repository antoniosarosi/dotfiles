Idioma
🇪🇸
[🇺🇸](https://github.com/antoniosarosi/dotfiles/tree/master/.xmonad)


Esta es la forma de usar mis configuraciones de *Xmonad*:

```bash
# Primero, instala las dependencias
sudo pacman -S xmonad xmonad-contrib xmobar
yay -S nerd-fonts-ubuntu-mono

# Clona este repositorio y copia mis configuraciones
git clone https://github.com/antoniosarosi/dotfiles.git
cp -r dotfiles/.xmonad ~
cp -r dotfiles/.config/xmobar ~/.config
```

Compila *Xmonad* y deberías poder iniciar sesión o testearlo con
**[Xephyr](https://wiki.archlinux.org/index.php/Xephyr)**:

```bash
xmonad --recompile
Xephyr -br -ac -noreset -screen 1280x720 :1 &
DISPLAY=:1 xmonad
```

Si ves que lanza *Xmobar*, sabes que la configuración es correcta. Modifica
las instancias de *Xmobar* según la cantidad de monitores que tienes. Así es
como los tengo yo:

```haskell
main = do
    -- Xmobar
    xmobarLaptop <- spawnPipe "xmobar -x 0 ~/.config/xmobar/laptop.hs"
    xmobarMonitor <- spawnPipe "xmobar -x 1 ~/.config/xmobar/monitor.hs"
```

Por ejemplo, si solo quieres una barra, borra la línea de *xmobarMonitor*. Si
quieres 3, copia y pega esa línea y cambiale el nombre a la tercera barra.
También tienes que modificar la línea siguiente para eliminar una instancia de
*Xmobar* o añadir una nueva.

```haskell
ppOutput = \x -> hPutStrLn xmobarLaptop x >> hPutStrLn xmobarMonitor x,
```

Solo una barra:

```haskell
ppOutput = \x -> hPutStrLn xmobarLaptop x
```

Tres barras:

```haskell
ppOutput = \x -> hPutStrLn xmobarLaptop x >> hPutStrLn xmobarMonitor1 x >> hPutStrLn xmobarMonitor2 x,
```

Una vez eso está hecho, puedes iniciar sesión. Pero recuerda que los atajos de
teclado no funcionarán a no ser que tengas todos los programas que uso yo y las
mismas configuraciones. Puedes cambiar los atajos de teclado o bien instalar el
software que uso yo, mira
[esta sección](https://github.com/antoniosarosi/dotfiles#keybindings)
para las instrucciones.
