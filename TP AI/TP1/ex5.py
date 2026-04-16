from sympy import symbols
from sympy.logic.boolalg import truth_table, Implies, And, Or, Not, Equivalent
#Définition des variables
expression=input("Saisir votre expression logique")
A = input("Saisir la valeur de A (True/False)")
B = input("Saisir la valeur de B (True/False)")
C = input("Saisir la valeur de C (True/False)")
result = expression
for i in range(len(expression)): 
    if expression[i] in('A','B','C'):
        result=result.replace(expression[i],bool(expression[i]))
result = eval(result)
print(f"A: {A}, B: {B}, C: {C} => expression logique : {result}")



def interact():
    expr=input("donner une expression logique")
    l=[]
    for v in expr:
        if v.isalpha() and v not in l:
            l.append(v)

    valeurs = {}
    for v in l:
        value = input(f"Valeur de {v}  : ")
        valeurs[v] = value == "True"
    result=eval(expr,valeurs)
    print(result)
interact()
#definir les variables and dans eval