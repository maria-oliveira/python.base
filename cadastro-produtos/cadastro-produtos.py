"""
Cadastro de Produtos.

"""

produto = {
    "nome" : "Caneta",
    "cores" :["azul", "branco"],
    "preco" : 3.23,
    "dimensoes" :{
    "altura":12.1,
    "largura":0.8
    },
    "em_estoque" :True,
    "codigo" :45678,
    "codebar" : None
}

cliente = {
    "nome": "Bruno"
}

compra ={
    "cliente": cliente,
    "produto": produto,
    "quantidade": 3
}
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
totalCompra = compra["quantidade"] *compra["produto"]["preco"]

print(
    f"{compra [ 'cliente' ] [ 'nome' ]}"
    f" comprou {compra ['quantidade'] } unidades de  {compra ['produto'] ['nome']}"
    f" e pagou o total de {totalCompra}"
)