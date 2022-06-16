from decimal import Decimal
from fractions import Fraction

print(bool(None), bool(False), bool(True))
# False False True
print(type(0j), type(Decimal(0)), type(Fraction(0, 1)))
# <class 'complex'> <class 'decimal.Decimal'> <class 'fractions.Fraction'>
print(bool(0), bool(0.0), bool(0j), bool(Decimal(0)), bool(Fraction(0, 1)))
# False False False False False
print(type(()), type({}), type(set()), type(range(0)))
# <class 'tuple'> <class 'dict'> <class 'set'> <class 'range'>
print(bool(''), bool(()), bool([]), bool({}), bool(set()), bool(range(0)))
# False False False False False False
