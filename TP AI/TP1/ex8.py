from sympy import And, Function, Implies, symbols

def pour_tout_x(E, reussit):
    for personne in E:
        if not reussit(personne):
            return False
    return True

def existe(E, reussit):
    for personne in E:
        if reussit(personne):
            return True
    return False

def reussit(personne):
    return personne in {'Alice', 'Bob'}  

# Alice et Bob réussissent, Charlie échoue
E={'Alice', 'Bob', 'Charlie'}
x= symbols('x')

#Définition de la formule
expression = And(pour_tout_x(E, reussit), existe(E, reussit))
print(f"Expression: {expression}")

