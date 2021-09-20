import re

def parse(content):
    imports = re.findall("(import (.+\.sh))", content)
    result = content
    for file in imports:
        f = open(file[1], "r")
        file_content = f.read()
        result = re.sub(file[0], file_content, result)
        f.close()

    return result
