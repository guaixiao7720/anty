

class CppCompiler:
    anty_code: str
    cpp_code: str
    output_path: str

    def __init__(self, anty_code_path, output_path):

        self.output_path = output_path
        with open(anty_code_path, "r") as anty_code_file:
            self.anty_code = anty_code_file.read()


    def complie(self):
        pass