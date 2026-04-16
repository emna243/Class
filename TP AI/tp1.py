def negation(x):
    return not(x);
def conjonction(a, b):
    return a and b;
def disjonction(a, b):
    return a or b;
def implication(a, b):
    return (not a) or b;
def equivalence(a, b):
    return a == b;
def testAll():
    for a in [True, False]:
        for b in [True, False]:
            print(f"a: {a}, b: {b} => "
                  f"negation(a): {negation(a)}, "
                  f"conjonction(a, b): {conjonction(a, b)}, "
                  f"disjonction(a, b): {disjonction(a, b)}, "
                  f"implication(a, b): {implication(a, b)}, "
                  f"equivalence(a, b): {equivalence(a, b)}")
testAll()

