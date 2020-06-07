import re
from silo.file_types.base_file_structure import FileStructure
import silo.file_types.utils as utils


class PurifiedImports:
    def __init__(self, imported_names, import_from_path):
        self.default = utils.purify_default_import_name(imported_names)
        self.imported_names = utils.purify_import_names(imported_names)
        self.import_from_path = import_from_path


class TestStructure(FileStructure):
    def __init__(self, path_to_file):
        super().__init__(path_to_file)
        self.file_imports = []
        self.update_contents()

    def read_imports(self):
        for line in self.contents:
            if utils.is_import.search(line):
                self.handle_line_import(line)

    def handle_line_import(self, line):
        split_from = line.split('from')
        code_path = utils.purify_code_path(split_from[1])
        code_imports = utils.purify_code_imports(split_from[0])
        self.file_imports.append(PurifiedImports(imported_names=code_imports, import_from_path=code_path))


'''
A few ways to import through JS:

1   import defaultExport from "module-name";
2   import * as name from "module-name";
3   import { export1 } from "module-name";
4   import { export1 as alias1 } from "module-name";
5   import { export1 , export2 } from "module-name";
5   import { foo , bar } from "module-name/path/to/specific/un-exported/file";
7   import { export1 , export2 as alias2 , [...] } from "module-name";
8   import defaultExport, { export1 [ , [...] ] } from "module-name";
9   import defaultExport, * as name from "module-name";
10  import "module-name";
11  var promise = import("module-name");

File structure to consider:

../MathSimulations/src/home/message-card.test.js
../MathSimulations/src/home/airplane-scene.test.js
../MathSimulations/src/commonroom/physics.test.js
../MathSimulations/src/commonroom/navbar.test.js
../MathSimulations/src/commonroom/canvas-images/image-size.test.js
../MathSimulations/src/commonroom/canvas-images/image-position.test.js

../MathSimulations/src/index.js
../MathSimulations/src/App.js
../MathSimulations/src/home/index.js
../MathSimulations/src/home/message-card.js
../MathSimulations/src/home/airplane-scene.js
../MathSimulations/src/sponsors/sponsor.js
../MathSimulations/src/simulations/index.js
../MathSimulations/src/simulations/counting/soccer.js
../MathSimulations/src/commonroom/navbar.js
../MathSimulations/src/commonroom/scene_base.js
../MathSimulations/src/commonroom/colors.js
../MathSimulations/src/commonroom/physics.js
../MathSimulations/src/commonroom/canvas-images/image-base.js
../MathSimulations/src/commonroom/canvas-images/background.js
../MathSimulations/src/commonroom/canvas-images/image-factory.js
../MathSimulations/src/commonroom/canvas-images/plane.js
../MathSimulations/src/commonroom/canvas-images/carousel.js
../MathSimulations/src/commonroom/canvas-images/ball.js
'''
