from sympy import symbols 
from sympy.logic.boolalg import truth_table, Implies, And
P, Q, R = symbols('P Q R')
expression_logique = And(Implies(P, Q), Implies(Q, R))

results = []
for values, result in truth_table(expression_logique, [P, Q, R]):
    p_value, q_value, r_value = values
    impl1=Implies(p_value, q_value)
    impl2=Implies(q_value, r_value)
    result = impl1 and impl2
    results.append(result)
    print(f"P: {p_value}, Q: {q_value}, R: {r_value} => expression logique : {result}")

if all(results):
    print("L'expression logique est une tautologie.")
elif not(all(results)):  
    print("L'expression logique est une contradiction.")
else:
    print("L'expression logique est une contigentce.")
