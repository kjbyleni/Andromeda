import os
import sys
from filing import Cabinet


# Want to have a list of files that do not have associated test file

cabinet = Cabinet()
cabinet.organize_files()
cabinet.print_test_files_locations()
cabinet.print_code_files_locations()


cabinet.test_folder.print_folder_contents()

