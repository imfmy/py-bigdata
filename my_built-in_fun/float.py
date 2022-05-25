print(float(' -Infinity'), float('+inf '))
# -inf inf
print(float('nan'), float('NAn'))
# nan nan
print(float())
# 0.0
print(float(float('   -12345\n')))
# -12345.0
print(float('1e-003'),float('1e3'))
# 0.001 1000.0
