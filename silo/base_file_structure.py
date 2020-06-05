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
