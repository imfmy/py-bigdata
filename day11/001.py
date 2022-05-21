import os
import sys
print('__file__ = ',__file__)
print('os.path.abspath(__file__)=',os.path.abspath(__file__))

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(base_dir)