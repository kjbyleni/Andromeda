import pytest
from silo.errors import DirectoryNotSpecifiedError
from silo.cabinet import Cabinet
from silo.folder_types.base_folder_structure import FolderStructure

PATH_TO_FAKE_SRC_FOLDER = './data_for_tests/fake_src_folder/'
PATH_TO_FAKE_SPEC_FILE = './data_for_tests/fake_src_folder/components/fake.spec.js'
PATH_TO_FAKE_TEST_FILE = './data_for_tests/fake_src_folder/fake.test.js'
PATH_TO_FAKE_JS_CODE_FILE = './data_for_tests/fake_src_folder/components/fake.js'


@pytest.fixture
def initial_cabinet_state():
    yield Cabinet()


def test_initial_state_test_folder_exists(initial_cabinet_state):
    assert isinstance(initial_cabinet_state.test_folder, FolderStructure)


def test_initial_state_code_folder_exists(initial_cabinet_state):
    assert isinstance(initial_cabinet_state.code_folder, FolderStructure)


def test_no_dir_throws_error(initial_cabinet_state):
    with pytest.raises(DirectoryNotSpecifiedError) as errInfo:
        initial_cabinet_state.organize_files()
    assert "You must specify a director" in str(errInfo.value)


@pytest.fixture
def file_cabinet(initial_cabinet_state):
    initial_cabinet_state.organize_files(PATH_TO_FAKE_SRC_FOLDER)
    yield initial_cabinet_state


'''Tests for test files'''


def test_organize_files_sorts_spec_files(file_cabinet):
    assert file_cabinet.test_folder.find_file(PATH_TO_FAKE_SPEC_FILE).contents[
               0] == '//spec file for testing'


def test_organize_files_sorts_test_files(file_cabinet):
    assert file_cabinet.test_folder.find_file(PATH_TO_FAKE_TEST_FILE).contents[
               0] == '//test file for testing\n'


'''Tests for Code files'''


def test_organize_files_sorts_js_files(file_cabinet):
    assert file_cabinet.code_folder.find_file(PATH_TO_FAKE_JS_CODE_FILE).contents[
               0] == '//js file for testing\n'


'''Test for other files'''


def test_other_files_sorts_txt_files(file_cabinet):
    assert file_cabinet.others == ['./data_for_tests/fake_src_folder/textDocument.txt']
