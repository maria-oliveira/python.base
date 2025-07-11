"""
Bloco de Notas

$notes.py new "Minha nota"
tag: tech
text:
...
$notes.py read --tag--tech 
...
"""

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")
cmds =("read", "read")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print("you must specify subcommand")
    sys.exit(1)

if arguments[0] not in cmds:
    print("Invalid command {argument[0]}")

if arguments[0] == "read":
 for line in open(filepath):
    titulo, tag, texto = line.splt("\t")
if tag == arguments[1].lower():
        print(f"titulo: {titulo}")
        print(f"text: {text}")

if arguments[0] == "new":
    titulo = arguments[1]
    text = [
        (f"{titulo}"),
        input("tag: ").strip(),
        input("text:\n ").strip(),
        "\n"
    ]  

with open (filepath,"a") as file_:
    file_.write("\t".join(text)+ "\n")