import os
import shutil
from typing import List
from unittest import TestCase, main

files_origin = [
    './test_files/folder_1/sub_folder_1/file_1.txt',
    './test_files/folder_1/sub_folder_2/file_2.txt',
    './test_files/folder_1/file_3.txt',
    './test_files/folder_1/file_4.txt'

]
folder_destination = [
    './test_files/folder_2/'
]

files_destination = [
    './test_files/folder_2/file_1.txt',
    './test_files/folder_2/file_2.txt',
    './test_files/folder_2/file_3.txt',
]

cvs_name_files = r'./test_files/list_name_files.csv'


def create_mock_folder(foldernames):
    for foldername in foldernames:
        os.makedirs(os.path.dirname(foldername), exist_ok=True)


def create_mock_files(filenames: list) -> None:
    for filename in filenames:
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w") as f:
            f.write("")


def create_mock_files_write(filenames: List[List[str]]):
    """
    :param filenames: [[filename, text_write], [filename, text_write]]
    :return:
    """
    for filename in filenames:
        os.makedirs(os.path.dirname(filename[0]), exist_ok=True)
        with open(filename[0], "w") as f:
            f.write(filename[1])


def rollback_mock_path(foldernames):
    for foldername in foldernames:
        shutil.rmtree(foldername, ignore_errors=True)


def check_file_exists(filenames: list) -> List[bool]:
    exist_files: List[bool] = []
    for filename in filenames:
        exist_files.append(os.path.isfile(filename))
    return exist_files


class TestMoveFiles(TestCase):

    def setUp(self):
        create_mock_files(files_origin)
        create_mock_folder(folder_destination)
        create_mock_files_write([
            [cvs_name_files, 'file_1.txt\nfile_2.txt\nfile_3.txt']
        ])

    def tearDown(self):
        rollback_mock_path([r'./test_files'])

    def test_go_moved_files(self):
        command = r"python __main__.py " \
                  r"--root_path=.\test_files\folder_1 " \
                  r"--destination_path=.\test_files\folder_2 " \
                  r"--csv_file_path=.\test_files\list_name_files.csv "
        os.system(command)
        files_moved = check_file_exists(files_destination)

        self.assertEqual(files_moved, [True, True, True])


main()
