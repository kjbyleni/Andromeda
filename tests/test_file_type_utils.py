import pytest
import silo.file_types.utils as utils

'''purify_code_path tests'''


def test_purify_code_removes_single_quotes():
    path_from_import = "'/path.js'"
    assert utils.purify_code_path(path_from_import) == "/path.js"


def test_purify_code_removes_double_quotes():
    path_from_import = '"/path.js"'
    assert utils.purify_code_path(path_from_import) == '/path.js'


def test_purify_code_removes_semicolon():
    path_from_import = '/path.js;'
    assert utils.purify_code_path(path_from_import) == '/path.js'


def test_purify_code_removes_single_double_quote_and_semicolon():
    single_quote = "'../'"
    double_quote = '"../"'
    semicolon = "path.js;"
    path_from_import = f'{single_quote}{double_quote}{semicolon}'
    assert utils.purify_code_path(path_from_import) == '../../path.js'


'''purify_code_imports tests'''


def test_import_key_word_is_removed():
    phrase = 'import exportName'
    assert utils.purify_code_imports(phrase) == 'exportName'


'''purify_names tests'''


def test_single_non_default_export():
    imported_names_string = '{ import1 }'
    assert utils.purify_import_names(imported_names_string) == ['import1']


def test_multiple_non_default_export():
    imported_names_string = '{ import1, import2, import3 }'
    assert utils.purify_import_names(imported_names_string) == ['import1', 'import2', 'import3']


def test_with_default_export():
    imported_names_string = 'defaultImport'
    assert utils.purify_import_names(imported_names_string) == []


def test_with_default_export_and_non_default_export():
    imported_names_string = 'defaultImport, { import1 }'
    assert utils.purify_import_names(imported_names_string) == ['import1']


def test_with_default_export_and_non_default_export_default_after_import():
    imported_names_string = '{ import1 }, defaultImport'
    assert utils.purify_import_names(imported_names_string) == ['import1']


'''purify_default tests'''


def test_default():
    imported_names_string = 'defaultImport'
    assert utils.purify_default_import_name(imported_names_string) == imported_names_string


def test_default_with_single_non_default():
    imported_names_string = 'defaultImport, {export1}'
    assert utils.purify_default_import_name(imported_names_string) == 'defaultImport'


def test_default_with_multiple_non_default():
    imported_names_string = 'defaultImport, {export1, export2}'
    assert utils.purify_default_import_name(imported_names_string) == 'defaultImport'


def test_default_at_end_with_multiple_non_default():
    imported_names_string = '{export1, export2}, defaultImport'
    assert utils.purify_default_import_name(imported_names_string) == 'defaultImport'
