import datetime
import os

from inline_args.inline_args import get_params_sys_args
from text_colorized.text_colorized import console
import func

console.header(f"INITIALIZED THE COPY PROCESS: {datetime.datetime.now()}")

sys_args = get_params_sys_args(['--root_path=', '--destination_path=', '--csv_file_path='])
__example_command_run = r"Example: python __main__.py --root_path=C:\Users\Downloads --destination_path=C:\User" \
                        r"s\Pictures --csv_file_path=C:\Users\Downloads\list_name_pictures.csv"

try:
    original_path = sys_args['--root_path=']  # original path absolute of files
except KeyError:
    raise ValueError(f"Set the '--root_path=' original path absolute of files origin\n {__example_command_run}")

try:
    destination_path = sys_args['--destination_path=']  # destination path absolute of files
except KeyError:
    raise ValueError(f"Set the '--destination_path=' argument destination path absolute of files\n {__example_command_run}")

try:
    csv_named_files = sys_args['--csv_file_path=']  # destination path absolute of files
except KeyError:
    raise ValueError(f"Set the '--csv_file_path=' argument with path csv with write files for move\n {__example_command_run}")

list_files = func.convert_cvs_in_set(path_csv=csv_named_files)

for idx, file in enumerate(list_files):
    try:
        path_root_file = func.find_file(path_root=original_path, name_file=file)
        func.copy_file(path_file=path_root_file, path_destination=os.path.join(destination_path, file))
        console.assertion(f"{idx} :: {file} :: File moved for path of destination")
    except Exception as e:
        console.fail(f"{idx} :: {file} :: File not moved for path of destination")

console.footer(f"FINISHED THE COPY PROCESS: {datetime.datetime.now()}")
