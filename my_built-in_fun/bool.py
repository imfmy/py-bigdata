print(('', bool('')), (0, bool(0)), ([], bool([])))
# ('', False) (0, False) ([], False)
print(('0', bool('0')), (1, bool(1)),([''],bool([''])))
# ('0', True) (1, True) ([''], True)
