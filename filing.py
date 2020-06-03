import os


class FileStructure:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        self.contents = []

    def update_contents(self):
        with open(self.path_to_file, 'r') as code:
            self.contents = code.readlines()

    def print_contents(self):
        for line in self.contents:
            print(line)


class FolderStructure:
    def __init__(self):
        self.folder_contents = {}

    def add_file(self, file_path):
        if file_path not in self.folder_contents:
            self.folder_contents[file_path] = FileStructure(file_path)
            self.folder_contents[file_path].update_contents()

    def print_paths(self):
        for path in self.folder_contents:
            print(path)
        print('\n\n\n')

    def find_file(self, key):
        return self.folder_contents[key]

    def print_folder_contents(self):
        for file_location in self.folder_contents:
            self.folder_contents[file_location].print_contents()


class Cabinet:
    def __init__(self):
        self.test_folder = FolderStructure()
        self.code_folder = FolderStructure()

    def organize_files(self, dir_to_walk=None):
        if dir_to_walk is None:
            print("need a dir")
            return
        for path, subdirs, files in os.walk(dir_to_walk):
            for name in files:
                if "test" in name or "spec" in name:
                    self.test_folder.add_file(os.path.join(path, name))
                else:
                    self.code_folder.add_file(os.path.join(path, name))

    def print_test_files_locations(self):
        self.test_folder.print_paths()

    def print_code_files_locations(self):
        self.code_folder.print_paths()

