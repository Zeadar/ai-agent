import os
import sys
import subprocess

TIMEOUT = 30


def run_python_file(working_directory, file_path, args=[]):
    working_directory = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not full_path.startswith(working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(full_path):
        return f'Error: File "{file_path}" not found.'

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        run_args = [sys.executable, file_path]
        if isinstance(args, list):
            run_args.extend(args)
        result = subprocess.run(
            run_args,
            capture_output=True,
            text=True,
            timeout=TIMEOUT,
            cwd=working_directory,
            check=True,
        )

    except subprocess.CalledProcessError as e:
        return f"Error: executing Python file: {e}"

    result_str = f"STDOUT: {result.stdout}\nSTDERR: {result.stderr}"

    if result.returncode != 0:
        result_str += f"\nProcess exited with code {result.returncode}"

    return result_str
