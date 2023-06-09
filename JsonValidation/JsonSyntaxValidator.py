import os
import json5


class JsonSyntaxValidator:
    def __init__(self, directory):
        """
        Initialize the JsonSyntaxValidator object.

        Args:
            directory (str): Directory path to validate JSON files.
        """
        self.__directory = directory
        self.__errors = []

    def validate_all_json_files(self):
        """
        Validate all JSON files in the specified directory.

        Returns:
            bool: True if all JSON files are valid, False otherwise.
        """
        for root, dirs, files in os.walk(self.__directory):
            for file in files:
                if file.endswith('.json'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as f:
                        try:
                            json5.load(f)
                        except ValueError as e:
                            error_msg = f'Invalid JSON in file {file_path}: {str(e)}'
                            self.__errors.append(error_msg)

        if self.__errors:
            print(self.__errors)
            return False

        return True
