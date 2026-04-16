from sympy import symbols
from sympy.logic.boolalg import truth_table, Implies, And, Or, Not, Equivalent

def verifier_tautologie(expression, nom):
    print(f"\nExpression: {nom}")
    
    A, B = symbols('A B')
    results = []
    for (A, B), result in truth_table(expression, [A, B]):
        results.append(result)
        print(f"A: {A}, B: {B} => {result}")
    
    if all(results):
        classification = "tautologie"
    elif not any(results):
        classification = "contradiction"
    else:
        classification = "contingence"
    
    print(f"L'expression est une {classification}.")
    return classification

# Définition des expressions
A, B = symbols('A B')

expr1 = Equivalent(Implies(A, B), Or(Not(A), B))
expr2 = Implies(And(A, B), A)
expr3 = Implies(A, Or(A, B))

# Vérification des trois expressions
verifier_tautologie(expr1, "(A => B) <=> (not A or B)")
verifier_tautologie(expr2, "(A and B) => A")
verifier_tautologie(expr3, "A => (A or B)")
