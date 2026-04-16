from sympy import Function, Implies, symbols 
x= symbols('x')
#Définition des prédicats
Mamifere = Function('Mamifereee')
Allaite = Function('Allaite')
#Définition de la formule
expression =Implies (Mamifere(x), Allaite(x))
print(f"Expression: {expression}")