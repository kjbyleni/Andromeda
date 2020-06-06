from silo.file_types.base_file_structure import FileStructure


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
            self.folder_contents[file_location].get_contents_as_single_line()
