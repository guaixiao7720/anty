import re

from .BlockCompiler import BlockCompiler


class CppCompiler:

    def __init__(self, anty_code_paths: str, output_path: str):
        self.anty_code_path_list: list[str]
        self.cpp_code: str
        self.output_path: str
        self.block: BlockCompiler
        self.__final_block_cache = None

        self.anty_code_path_list = anty_code_paths.split(",")

        self.output_path = output_path
        for anty_code_path in self.anty_code_path_list:
            with open(anty_code_path, "r") as anty_code_file:
                anty_code = anty_code_file.read()
                self.compile(anty_code)


    def compile(self, anty_code: str) -> str:
        self.block = BlockCompiler(0)
        indentation_num: int = 0
        for index, statement_str in enumerate(re.split(r"[\n']", anty_code)):
            indentation: int = len(re.findall(r"( {4}|\t)", statement_str))
            # print(indentation)
            if indentation == 0:
                indentation_num = 0
            else:
                if indentation_num != indentation:
                    indentation_num = indentation
                    final_block: BlockCompiler = self.get_final_block(indentation_num - 1)
                    final_block.blocks.append(BlockCompiler(indentation_num, final_block))


        print("12121")




    def get_final_block(self, indentation_num: int) -> BlockCompiler | None:
        if indentation_num == 0:
            return self.block

        self.__final_block_cache = None

        for block in self.block.blocks:
            self._final_block(indentation_num, block)

        if self.__final_block_cache is None:
            return None
        else:
            return self.__final_block_cache

    def _final_block(self, indentation_num: int, block: BlockCompiler):
        for block_1 in block.blocks:
            self._final_block(indentation_num, block_1)

        if indentation_num == block.indentation_num:
            self.__final_block_cache = block
