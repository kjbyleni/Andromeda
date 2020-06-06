class FileStructure:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file
        self.contents = []

    def update_contents(self):
        with open(self.path_to_file, 'r') as code:
            self.contents = code.readlines()

    def get_contents_as_single_line(self):
        content_str = ''
        for line in self.contents:
            content_str += f' {line}'
        return content_str
