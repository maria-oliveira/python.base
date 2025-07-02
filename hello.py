"""
hello word multi linguas
dependendo da lingua configurada no ambiente o programa exibe a 
mensagem corespondente

Como usar:
tenha a variavel LANG devidadamente configurada ex:
export LANG=pt_BR

Execução:
python hello.py   
ou 
 ./hello.py
"""
__version__ = "0.0.1"
__author__="Maria Eduarda Oliveira"
import os

current_language= os.getenv("LANG")[:5]

mensagem = "Hello world!"

if current_language == "pt_BR" :
    mensagem= "Ola mundo!"
elif current_language =="it_IT":        
    mensagem = "Ciao, Mondo!"


print(mensagem)




