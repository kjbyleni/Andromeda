import re

is_import = re.compile("^import .+ from .+")
non_defaults = "{.+}"


def purify_code_path(code_path_from_import):
    pure_path = code_path_from_import.replace('"', '')
    pure_path = pure_path.replace(";", '')
    pure_path = pure_path.replace("'", '')
    return pure_path.strip()


def purify_code_imports(code_imports):
    pure_imports = code_imports.replace('import', '')
    return pure_imports.strip()


def purify_import_names(imported_names_string):
    purified_names = []
    non_default_imports = re.search(non_defaults, imported_names_string)
    if non_default_imports:
        purified = non_default_imports.group(0).replace("{", "")
        purified = purified.replace("}", "")
        purified = purified.replace(" ", "")
        purified_names = purified.split(',')

    return purified_names


def purify_default_import_name(imported_names_string):
    if '{' in imported_names_string:
        split_str = imported_names_string.split('{')
        if '{' not in split_str[0] and '' != split_str[0]:
            return split_str[0].replace(',', '').strip()
        else:
            split_str = imported_names_string.split('}')
            if '}' not in split_str[-1]:
                return split_str[-1].replace(',', '').strip()
            else:
                return None
    else:
        return imported_names_string
