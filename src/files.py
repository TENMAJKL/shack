import parser

def parse(file, new_name):
    f = open(file, "r")
    content = f.read()
    f.close()
    
    result = parser.parse(content)

    nf = open(new_name, "w")
    nf.write(result)
    nf.close()
