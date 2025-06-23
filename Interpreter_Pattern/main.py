from number import Number
from sign import Add, Subtract


eqn = "2 + 5 - 1 + 10"

tokens = eqn.split(' ')
print(tokens)

AST = []

AST.append(Add(Number(tokens[0]), Number(tokens[2])))
AST.append(Subtract(AST[0], Number(tokens[4])))
AST.append(Add(AST[1], Number(tokens[6])))

AST_Root = AST.pop()

print(AST_Root.interpret())

print(AST_Root)  # Printing the representation of the process
