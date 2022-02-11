import os
import shutil
import csv
from typing import List


def copy_file(path_file, path_destination):
    try:
        shutil.copy(path_file, path_destination)
    except Exception as e:
        raise ValueError(e)


def find_file(path_root: str, name_file: str) -> str:
    path = path_root
    for root, dirs, files in os.walk(path):
        for file in files:
            if file == name_file:
                return str(os.path.join(root, file))


def convert_cvs_in_set(path_csv: str) -> set:
    with open(path_csv, newline='') as f:
        reader = csv.reader(f)
        data: List[List[str]] = list(reader)
        flat_array_set = set([item for sublist in data for item in sublist])
    return flat_array_set
