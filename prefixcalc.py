import os
import sys

from datettime import datetime
arguments = sys.argv[1:]

if not arguments:
    operation = input("Qual e a operacao?:")
    n1 = input("n1:")
    n2= input("n2:")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print ("numero de argumentos invalidos!")
    print ("ex: sum 55")
    sys.exit(1)
operation, *nums= arguments

valid_operations =("sum", "sub", "mul", "div")
if operation not in valid_operations:
    print("Operacao invalida")
    print(valid_operations)
    sys.exit(1)

validated_nums =[]
for num in nums:
    if not num.replae(".", "").isdigit():
        print(f"Numero invalido {num}")
        sys.exit(1)
    else:
        num = int(num)
    validated_nums.append(num)

n1, n2 = validated_nums

if operation == "sum" :
    result = n1 + n2
elif operation == "sub" :
    result = n1 - n2
elif operation == "mul" :
    result = n1 * n2
elif operation == "div" :
    result = n1 / n2

path = os.curdir
filepath = os.path.join(path, "prefixcal.log")
timestamp = datetime.now().isoformat()

with open(filepath, "a") as file_:
    file_.write(f"{timestamp} - {operation},{n1},{n2} = {result}\n")

print ("O resultado e {result}")