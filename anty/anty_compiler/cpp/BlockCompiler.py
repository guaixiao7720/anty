

class BlockCompiler:

    def __init__(self, indentation_num: int, parent_block = None):
        self.variables: list[str] = []
        self.statements: list[StatementCompiler] = []
        self.blocks: list[BlockCompiler] = []
        self.indentation_num: int
        self.parent_block = None
        self.indentation_num = indentation_num
        self.parent_block = parent_block


class StatementCompiler:

    def __init__(self, parent_block: BlockCompiler):
        self.parent_block: BlockCompiler = parent_block