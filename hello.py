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

current_language = os.getenv("LANG", "en_US")[:5]

mensagem = {
    "en_US": "Hello, World!",
    "pt_BR":"Ola, Mundo!",
    "it_IT":"Ciao, Mondo!",
    "es_SP":"Hola, Mundo",
    "fr_FR":"Bonjour, Monde"

}


print(mensagem[current_language])




