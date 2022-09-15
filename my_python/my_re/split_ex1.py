import re

text = """Ross McFluff: 834.345.1254 155 Elm Street
  
Ronald Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way


Heather Albrecht: 548.326.4584 919 Park Place"""
t1 = re.split('[\n]+', text)
print(t1)
t2 = [e for e in t1]
print(t2)
t2 = [re.split(':? ', e, 3) for e in t1]
print(t2)
text = "Professor Abdolmalek, please report your absences promptly."
print(re.findall(r"(\w)(\w+)(\w)", text))
print(re.sub(r"(\w)(\w+)(\w)", '\g<3>\g<2>\g<1>', text))


def repl1(m):
    inner = list(m.group(2))
    r = reversed(inner)
    return m[1] + "".join(r) + m[3]


print(re.sub(r'(\w)(\w+)(\w)', repl1, text))
