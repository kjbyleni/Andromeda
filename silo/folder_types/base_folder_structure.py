from silo.file_types.base_file_structure import FileStructure


class FolderStructure:
    def __init__(self):
        self.folder_contents = {}

    def add_file(self, file_path):
        self.folder_contents[file_path] = FileStructure(file_path)
        self.folder_contents[file_path].update_contents()

    def find_file(self, key) -> FileStructure:
        return self.folder_contents[key]
