import pytest
from silo.folder_types.base_folder_structure import FolderStructure

PATH_TO_EMPTY_TEST_FILE = './data_for_tests/blank.txt'
PATH_TO_CONTENT_FILE = './data_for_tests/containsInformation.txt'


@pytest.fixture
def folder():
    f = FolderStructure()
    f.add_file(PATH_TO_CONTENT_FILE)
    yield f


def test_initial_state():
    initial_folder_state = FolderStructure()
    assert initial_folder_state.folder_contents == {}


def test_add_file_adds_file_to_folder(folder):
    assert PATH_TO_CONTENT_FILE in folder.folder_contents


def test_add_file_updates_contents_of_file(folder):
    assert folder.folder_contents[PATH_TO_CONTENT_FILE].contents[0] == 'Hello, This is a text test file.\n'


def test_get_paths_in_folder(folder):
    assert list(folder.folder_contents.keys())[0] == PATH_TO_CONTENT_FILE


def test_only_one_entry(folder):
    folder.add_file(PATH_TO_CONTENT_FILE)
    assert len(folder.folder_contents) == 1


def test_find_file_returns_file(folder):
    folder.add_file(PATH_TO_EMPTY_TEST_FILE)
    assert folder.find_file(PATH_TO_CONTENT_FILE).contents[0] == 'Hello, This is a text test file.\n'
