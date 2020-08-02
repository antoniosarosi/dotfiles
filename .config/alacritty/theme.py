#!/usr/bin/env python

from sys import argv
from os import path
import yaml


def change_theme(alacritty_file, theme_file):
    try:
        with open(alacritty_file) as f:
            alacritty = yaml.load(f, Loader=yaml.FullLoader)
        with open(theme_file) as f:
            theme = yaml.load(f, Loader=yaml.FullLoader)

        if "colors" not in theme:
            print('Theme "{}" has no color configuration'.format(theme_file))
            return False

        alacritty["colors"] = theme["colors"]

        with open(alacritty_file, "w") as f:
            yaml.dump(alacritty, f)

        return True

    except yaml.YAMLError as e:
        print((
            "YAML error at parsing file, "
            "at line {0.problem_mark.line}, "
            "column {0.problem_mark.column}:\n"
            "{0.problem} {0.context}\n"
        ).format(e))

    return False


def main():
    if len(argv) != 2:
        print("Usage:\n{} theme".format(argv[0]))
        exit(0)

    alacritty_path = path.join(path.expanduser("~"), ".config", "alacritty")
    alacritty_file = path.join(alacritty_path, "alacritty.yml")
    theme_file = path.join(alacritty_path, "themes", "{}.yaml".format(argv[1]))

    if not path.exists(theme_file):
        print("Theme file {} does not exist".format(theme_file))
        exit(0)

    if change_theme(alacritty_file, theme_file):
        print("Theme successfully changed")
    else:
        print("Could not change theme")


if __name__ == "__main__":
    main()
