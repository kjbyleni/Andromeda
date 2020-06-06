import os
import re

from silo.errors import DirectoryNotSpecifiedError
from silo.folder_types.base_folder_structure import FolderStructure

is_test_file = re.compile("test|spec")
is_code_file = re.compile("js|ts")


class Cabinet:
    def __init__(self):
        self.test_folder = FolderStructure()
        self.code_folder = FolderStructure()
        self.others = []

    def organize_files(self, dir_to_walk=None):
        if dir_to_walk is None:
            raise DirectoryNotSpecifiedError("You must specify a directory")
        for path, subdirs, files in os.walk(dir_to_walk):
            for name in files:
                if is_test_file.search(name):
                    self.test_folder.add_file(os.path.join(path, name))
                elif is_code_file.search(name):
                    self.code_folder.add_file(os.path.join(path, name))
                else:
                    self.others.append(os.path.join(path, name))

    def print_test_files_locations(self):
        self.test_folder.get_paths_in_folder()

    def print_code_files_locations(self):
        self.code_folder.get_paths_in_folder()
