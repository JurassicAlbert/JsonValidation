import os
from JsonSyntaxValidator import JsonSyntaxValidator


def main():
    project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    linter = JsonSyntaxValidator(project_directory)
    if not linter.validate_all_json_files():
        exit(1)


if __name__ == '__main__':
    main()
