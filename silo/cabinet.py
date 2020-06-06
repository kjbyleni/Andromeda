import os
import re

from silo.folder_types.base_folder_structure import FolderStructure

test_locator_regex = re.compile("test|spec")
code_locator_regex = re.compile("js|ts")



class Cabinet:
    def __init__(self):
        self.test_folder = FolderStructure()
        self.code_folder = FolderStructure()
        # self.other_folder = FolderStructure()

    def organize_files(self, dir_to_walk=None):
        if dir_to_walk is None:
            print("need a dir")
            return
        for path, subdirs, files in os.walk(dir_to_walk):
            for name in files:
                if test_locator_regex.search(name):
                    self.test_folder.add_file(os.path.join(path, name))
                elif code_locator_regex.search(name):
                    self.code_folder.add_file(os.path.join(path, name))
                else:
                    print("Other ->", name)

    def print_test_files_locations(self):
        self.test_folder.get_paths_in_folder()

    def print_code_files_locations(self):
        self.code_folder.get_paths_in_folder()
