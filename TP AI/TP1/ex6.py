from sympy import symbols
from sympy.logic.boolalg import truth_table, Implies, And, Or, Not, Equivalent

def verifier_tautologie(expression, nom):
    print(f"\nExpression: {nom}")
    
    A, B ,C = symbols('A B C')
    results = []
    for (A, B, C), result in truth_table(expression, [A, B, C]):
        results.append(result)
        print(f"A: {A}, B: {B}, C: {C} => {result}")
    
    if all(results):
        classification = "tautologie"
    elif not any(results):
        classification = "contradiction"
    else:
        classification = "contingence"
    
    print(f"L'expression est une {classification}.")
    return classification

# Définition des expressions
A, B, C = symbols('A B C')

expr1 = Implies(And(Implies(A, B), Implies(B, C)), Implies(A, C))


# Vérification des trois expressions
verifier_tautologie(expr1, "((A ⇒ B) ∧ (B ⇒ C)) ⇒ (A ⇒ C)")

