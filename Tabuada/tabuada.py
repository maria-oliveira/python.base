"""
Impime a tabuada do 1 ao 10.
----Tabuada do 1---
1 x 1 = 1
2 x 1 = 2
3 x 1 = 3
...

===================

----Tabuada do 2---
1 x 2 = 2
2 x 2 = 4
3 x 2 = 6
...

==================
"""

numeros = list(range(1, 11))

 # Loop externo para o primeiro número da multiplicação (n1
for n1 in numeros:
      print("{:-^18}".format(f"tabuada do {n1}"))
      print()
      # Loop interno para o segundo número da multiplicação (n2
      for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))

      print()

