import pytest
from silo.file_types.test_file import TestStructure

PATH_TO_EMPTY_TEST_FILE = './data_for_tests/blank.txt'
PATH_TO_CONTENT_FILE = './data_for_tests/containsInformation.txt'


@pytest.fixture
def empty_file():
    yield TestStructure(PATH_TO_EMPTY_TEST_FILE)


@pytest.fixture
def text_file():
    yield TestStructure(PATH_TO_CONTENT_FILE)


# def test_file_imports_is_empty_by_default(text_file):
#     text_file
