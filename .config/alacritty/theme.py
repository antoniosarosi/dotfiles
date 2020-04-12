from sys import argv
from os import path
import yaml


def change_theme(alacritty_file, theme_file):
    try:
        with open(alacritty_file) as f:
            alacritty = yaml.load(f, Loader=yaml.FullLoader)
        with open(theme_file) as f:
            theme = yaml.load(f, Loader=yaml.FullLoader)
         
        
        if "colors" in theme:
            alacritty["colors"] = theme["colors"]
        else:
            print("Theme \"{theme_file}\" has no color configuration.")
            return False

        with open(alacritty_file, "w") as f:
            yaml.dump(alacritty, f)
                  
    except PermissionError as e:
        print("Can't read/write {0.filename} : Not allowed".format(e))
    except yaml.YAMLError as e:
        print("YAML error at parsing file:\n at line {0.problem_mark.line}, column {0.problem_mark.column} : {0.problem} {0.context}".format(e))
    else:
        return True
    return False


def main():
    if len(argv) != 2:
        print("Usage:\npython {} theme.yaml".format(argv[0]))
        exit(0)
    
    if not path.exists(argv[1]):
        print("Theme file {} does not exist".format(argv[1]))
        exit(0)

    alacritty_path = path.join(
        path.expanduser("~"),
        ".config/alacritty/alacritty.yml"
    )
    if change_theme(alacritty_path, argv[1]):
        print("Theme successfully changed")
    else:
        print("Could not change theme.")


if __name__ == "__main__":
    main()
