from itertools import product 
for A, B in product([False, True], repeat=2):
    A_and_B = A and B
    A_or_B = A or B
    not_A = not A
    A_implies_B = (not A) or B
    A_equiv_B = A == B
    print(f"*******A: {A}, B: {B}*******\n "
          f"A and B: {A_and_B}| "
          f"A or B: {A_or_B}| "
          f"not A: {not_A}| "
          f"A implies B: {A_implies_B}| "
          f"A equivalent B: {A_equiv_B}\n")
for A, B, C in product([False, True], repeat=3):
    A_and_B_and_C = A and B and C
    A_or_B_or_C = A or B or C
    print(f"*******A: {A}, B: {B}, C: {C}*******\n "
          f"A and B and C: {A_and_B_and_C}| "
          f"A or B or C: {A_or_B_or_C}\n")