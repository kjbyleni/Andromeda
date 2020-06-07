import pytest
from silo.file_types.base_file_structure import FileStructure

PATH_TO_EMPTY_TEST_FILE = './data_for_tests/blank.txt'
PATH_TO_CONTENT_FILE = './data_for_tests/containsInformation.txt'


@pytest.fixture
def empty_file():
    yield FileStructure(PATH_TO_EMPTY_TEST_FILE)


@pytest.fixture
def text_file():
    yield FileStructure(PATH_TO_CONTENT_FILE)


'''Test empty file'''


def test_path_is_set_correctly(empty_file):
    assert empty_file.path_to_file is PATH_TO_EMPTY_TEST_FILE


def test_no_path_specified_contents_is_empty(empty_file):
    assert empty_file.contents == []


def test_update_contents_sets_contents_with_empty_file(empty_file):
    empty_file.update_contents()
    assert empty_file.contents == []


def test_get_contents_returns_nothing_when_empty_content(empty_file):
    empty_file.update_contents()
    assert empty_file.get_contents_as_single_line() == ''


'''Test files with content'''


def test_update_contents_sets_contents_as_array(text_file):
    text_file.update_contents()
    assert len(text_file.contents) == 2


def test_get_contents_returns_expected_when_file_contains_information(text_file):
    text_file.update_contents()
    assert text_file.get_contents_as_single_line() == ' Hello, This is a text test file.\n This Text file has multiple lines'


def test_folder_breakdown_get_seporated(text_file):
    assert len(text_file.folder_breakdown) == 3
