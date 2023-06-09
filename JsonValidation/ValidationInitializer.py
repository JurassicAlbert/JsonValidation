import os
from .JsonSyntaxValidator import JsonSyntaxValidator
from .JsonStructureValidator import JsonStructureValidator


class ValidationInitializer:
    """
    Class responsible for initializing and running JSON validators.
    """

    def __init__(self):
        """
        Initialize the ValidationInitializer object.
        Sets the project directory as the parent directory of the current file.
        """
        self.__project_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def run_json_syntax_validator(self):
        """
        Run the JSON syntax validator.

        Creates an instance of JsonSyntaxValidator and validates all JSON files in the project directory.
        If any JSON file is invalid, exit the program with code 1.
        """
        linter = JsonSyntaxValidator(self.__project_directory)
        if not linter.validate_all_json_files():
            exit(1)

    def run_json_structure_validator(self):
        """
        Run the JSON structure validator.

        Creates an instance of JsonStructureValidator and checks the structures of JSON files
        against the specified schema in the project directory.
        """
        structure_validator = JsonStructureValidator()
        structure_validator.check_json_structures(self.__project_directory)
