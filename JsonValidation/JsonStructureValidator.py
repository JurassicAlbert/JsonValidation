import json
import glob
import os


class JsonStructureValidator:
    def __init__(self, schema_file_name='schema.json'):
        """
        Initialize the JsonStructureValidator object.

        Args:
            schema_file_name (str): Name of the schema file (default: 'schema.json').
        """
        self.__schema_file_name = schema_file_name

    def check_json_structures(self, directory):
        """
        Check the structures of JSON files against the specified schema.

        Iterate over the directories in the specified directory and validate the JSON files within each directory
        against the corresponding schema file located in the 'Schema' subdirectory.
        Print whether the structure of each JSON file is valid or invalid.

        Args:
            directory (str): Parent directory containing the subdirectories with JSON files and schema files.
        """
        for root, dirs, files in os.walk(directory):
            if 'Schema' in dirs:
                schema_directory = os.path.join(root, 'Schema')
                schema_file = os.path.join(schema_directory, self.__schema_file_name)

                if os.path.isfile(schema_file):
                    json_files = glob.glob(os.path.join(root, '*.json'))
                    return self.validate_json_files(schema_file, json_files)

    def validate_json_files(self, schema_file, json_files):
        """
        Validate the JSON files against the specified schema file.

        Args:
            schema_file (str): Path to the schema file.
            json_files (list): List of paths to the JSON files.
        """
        with open(schema_file, 'r') as schema:
            schema_data = json.load(schema)

        for json_file in json_files:
            with open(json_file, 'r') as json_data:
                json_content = json.load(json_data)

            if self.validate_json_structure(schema_data, json_content):
                print(f"{json_file}: Structure is valid.")
            else:
                print(f"{json_file}: Structure is invalid.")

    def validate_json_structure(self, schema, json_data):
        """
        Validate the structure of JSON data against the specified schema.

        Args:
            schema (dict): JSON schema dictionary.
            json_data (dict): JSON data to validate.

        Returns:
            bool: True if the structure is valid, False otherwise.
        """
        for section, subsections in schema.items():
            if section not in json_data:
                return False

            for subsection, positions in subsections.items():
                if subsection not in json_data[section]:
                    return False

        return True


# Przykład użycia
validator = JsonStructureValidator()
validator.check_json_structures('directory_path')
