#JsonValidation

A small Python script created with the purpose of automating steps in project pull requests (PRs). The primary goal of this project is to enhance PRs by adding requirements and automated tests. This ensures that PRs cannot be merged into other branches if they contain invalid syntax that wasn't identified by the committer. The aim is to prevent the use of JSON data models and fixtures in the project that might fail due to incorrect formatting.

##Version 0.01:

    - Implemented a script that validates JSON format, detects unexpected commas, brackets, and syntax errors.
    - Added a workflow test that checks if the script identifies errors in incorrect JSONs.
    - Included a workflow test that verifies if the script successfully passes for correct JSONs.

##Planned for Version 0.02:

    - Enhance the script to validate the content and fields of JSON data models based on a specific template. Fields within data models should match the expected template format.
    - Introduce a workflow test to identify errors in JSON data models with incorrect content or fields.
    - Implement a workflow test to ensure the script successfully passes for JSON data models with correct content and fields.
