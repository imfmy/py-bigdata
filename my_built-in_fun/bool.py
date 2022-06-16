from decimal import Decimal
from fractions import Fraction

print(('', bool('')), (0, bool(0)), ([], bool([])))
# ('', False) (0, False) ([], False)
print(('0', bool('0')), (1, bool(1)), ([''], bool([''])))
# ('0', True) (1, True) ([''], True)
if 2>1 and print('2>1') or print('2<1'):
    pass

