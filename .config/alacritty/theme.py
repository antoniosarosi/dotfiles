from sys import argv
from os import path
import yaml


def change_theme(alacritty_file, theme_file):
    with open(alacritty_file) as f:
        alacritty = yaml.load(f, Loader=yaml.FullLoader)
    with open(theme_file) as f:
        theme = yaml.load(f, Loader=yaml.FullLoader)

    alacritty["colors"] = theme["colors"]

    with open(alacritty_file, "w") as f:
        yaml.dump(alacritty, f)


def main():
    if len(argv) != 2:
        print("Usage:\npython {} theme.yaml".format(argv[0]))
        exit(0)

    if not path.exists(argv[1]):
        print("Theme file {} does not exist".format(argv[1]))
        exit(0)

    change_theme("alacritty.yml", argv[1])
    print("Theme successfully changed")


if __name__ == "__main__":
    main()
