import re

class CppCompiler:
    anty_code_path_list: list[str]
    cpp_code: str
    output_path: str


    def __init__(self, anty_code_paths: str, output_path: str):
        self.anty_code_path_list = anty_code_paths.split(",")

        self.output_path = output_path
        for anty_code_path in self.anty_code_path_list:
            with open(anty_code_path, "r") as anty_code_file:
                anty_code = anty_code_file.read()
                self.compile(anty_code)


    def compile(self, anty_code: str) -> str:
        code_lines_str: list[str] = re.split(r"[\n`]", anty_code)

        for code_line in code_lines_str:
            indentation_num: int = len(re.findall(r"( {4}|\t)", code_line))