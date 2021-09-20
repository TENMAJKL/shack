from os.path import exists
from files import parse

def cli(args):
    if len(args) < 2:   
        print(f"Not enought arguments")
        return
    if not exists(args[1]):
        print(f"File {args[1]} doesn't exist")
        return
    
    parse(args[1], args[2])

