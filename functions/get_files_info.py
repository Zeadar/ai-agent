import os


def get_files_info(working_directory, directory="."):
    working_directory = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, directory))

    if not os.path.isdir(working_directory):
        return f'Error: "{working_directory}" is not a directory'

    if not full_path.startswith(working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'

    try:
        files = os.listdir(full_path)
        files = map(
            lambda filename: f"- {filename}: file_size={os.path.getsize(os.path.join(full_path, filename))} bytes, is_dir={os.path.isdir(os.path.join(full_path, filename))}",
            files,
        )
    except OSError as e:
        return f"Error: (OSError) {e}"

    return "\n".join(list(files))
