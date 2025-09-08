import os


MAX_BYTES = 10000


def get_file_content(working_directory, file_path):
    working_directory = os.path.abspath(working_directory)
    full_path = os.path.join(working_directory, file_path)

    if not full_path.startswith(working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(full_path, "r") as f:
            file_content_string = f.read(MAX_BYTES)

            if len(file_content_string) == MAX_BYTES:
                file_content_string += (
                    f'[...File "{file_path}" truncated at {MAX_BYTES} characters]'
                )

            return file_content_string

    except OSError as e:
        return f"Error: {e}"
