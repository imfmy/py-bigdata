def make_pizza(size=8, *ingredients):
    """通过输入的尺寸与材料制作披萨"""
    print(f'we will make a {size}\' pizza  with the following ingredients:')
    for e in ingredients:
        print(f'- {e}')


def sell_pizza(size, *ingredients):
    """通过输入披萨的尺寸和材料,可以输入披萨的出售价格"""
    print(f'The price of {size} inch pizza is {size * (len(ingredients))}$')
