from silo.cabinet import Cabinet
from search_dir import DIRECTORY_TO_SEARCH

# Want to have a list of files that do not have associated test file

cabinet = Cabinet()
cabinet.organize_files(DIRECTORY_TO_SEARCH)
cabinet.print_test_files_locations()
cabinet.print_code_files_locations()
