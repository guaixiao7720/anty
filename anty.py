import argparse

import anty

# parser = argparse.ArgumentParser(description="111")
#
# parser.add_argument("code_path", type = str, help="The path of the Anty code")
# parser.add_argument("output_path", type = str, help="The path of the output code")
#
# args = parser.parse_args()
#
# anty_code_path: str = args.code_path
# output_code_path: str = args.output_path

if __name__ == '__main__':
    anty_code_path: str = "D:\\aaa.ant"
    output_code_path: str = "12"

    cpp_compiler: anty.anty_compiler.cpp.CppCompiler = anty.anty_compiler.cpp.CppCompiler(anty_code_path, output_code_path)


    print(str(cpp_compiler))