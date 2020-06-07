import pytest
from silo.file_types.test_structure import TestStructure, PurifiedImports

PATH_TO_FAKE_TEST_FILE = './data_for_tests/fake_src_folder/fake.test.js'
PATH_TO_NO_IMPORTS_FROM_FILE = './data_for_tests/fake_src_folder/components/noImportFrom.js'


@pytest.fixture
def imports_file():
    yield TestStructure(PATH_TO_FAKE_TEST_FILE)


def test_file_imports_is_empty_by_default(imports_file):
    assert imports_file.file_imports == []


def test_update_contents_is_called_by_default(imports_file):
    assert len(imports_file.contents) >= 1


def test_default_import(imports_file):
    imports_file.read_imports()
    assert isinstance(imports_file.file_imports[0], PurifiedImports)


def test_default_import_purifies_default_imports_names(imports_file):
    imports_file.read_imports()
    assert imports_file.file_imports[0].default == 'defaultExport'


def test_default_import_purifies_imports_path(imports_file):
    imports_file.read_imports()
    assert imports_file.file_imports[0].import_from_path == './components/fake.js'


def test_handle_line_imports_multiple_imports(imports_file):
    file_import = 'import a, {b, c} from "../../happy.js"'
    imports_file.handle_line_import(file_import)
    assert imports_file.file_imports[0].imported_names == 'a, {b, c}'


def test_handle_line_imports_multiple_imports(imports_file):
    file_import = 'import a, {b, c} from "../../happy.js"'
    imports_file.handle_line_import(file_import)
    assert imports_file.file_imports[0].import_from_path == '../../happy.js'


def test_when_import_excludes_from():
    no_from_imports = TestStructure(PATH_TO_NO_IMPORTS_FROM_FILE)
    no_from_imports.read_imports()
    assert no_from_imports.file_imports == []
