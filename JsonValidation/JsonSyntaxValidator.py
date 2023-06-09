import os
import subprocess


class JsonSyntaxValidator:
    def __init__(self, directory):
        self.__directory = directory

    def validate_all_json_files(self):
        for root, dirs, files in os.walk(self.__directory):
            for file in files:
                if file.endswith('.json'):
                    file_path = os.path.join(root, file)
                    command = f'jsonlint {file_path}'
                    result = subprocess.run(command, shell=True)
                    if result.returncode != 0:
                        print(f'Invalid JSON in file {file_path}')
                        return False
        return True
