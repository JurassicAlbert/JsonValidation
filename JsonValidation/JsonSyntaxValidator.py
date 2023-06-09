import os
import subprocess
import json5


class JsonSyntaxValidator:
    def __init__(self, directory):
        self.__directory = directory

        # def validate_all_json_files(self):
        #     for root, dirs, files in os.walk(self.__directory):
        #         for file in files:
        #             if file.endswith('.json'):
        #                 file_path = os.path.join(root, file)
        #                 command = f'jq {file_path}'
        #                 result = subprocess.run(command, shell=True, capture_output=True, text=True)
        #                 if result.returncode != 0:
        #                     error_message = result.stderr.strip()
        #                     print(f'Invalid JSON in file {file_path}: {error_message}')
        #                     return False
        #     return True

    def validate_all_json_files(self):
        for root, dirs, files in os.walk(self.__directory):
            for file in files:
                if file.endswith('.json'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r') as f:
                        try:
                            json5.load(f)
                        except ValueError as e:
                            print(f'Invalid JSON in file {file_path}: {str(e)}')
                            return False
        return True
