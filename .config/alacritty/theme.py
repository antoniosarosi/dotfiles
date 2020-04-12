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
        print("YAML error at parsing file, ", end="")
        print("at line {0.problem_mark.line}, ".format(e), end="")
        print("column {0.problem_mark.column}:".format(e))
        print("{0.problem} {0.context}\n".format(e))

    return False


def main():
    if len(argv) != 2:
        print("Usage:\npython {} theme.yaml".format(argv[0]))
        exit(0)

    if not path.exists(argv[1]):
        print("Theme file {} does not exist".format(argv[1]))
        exit(0)

    alacritty_path = path.join(
        path.expanduser("~"), ".config", "alacritty", "alacritty.yml"
    )

    if change_theme(alacritty_path, argv[1]):
        print("Theme successfully changed")
    else:
        print("Could not change theme")


if __name__ == "__main__":
    main()
