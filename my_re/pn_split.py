import re

pattern = re.compile('\d+')
print(pattern.split('ht9ln10vt11ff12cr13'))
# ['ht', 'ln', 'vt', 'ff', 'cr', '']
print(pattern.split('ht9ln10vt11ff12cr13', 3))
# ['ht', 'ln', 'vt', 'ff12cr13']
print(pattern.split('ht9ln10vt11ff12cr13'[3:10]))
# ['ln', 'vt', '']
p = re.compile('\d+[a-z]+', re.I)
print(p.split('ht9ln10vt11ff12cr13', 0))
# ['ht', '', '', '', '13']
p = re.compile('(\d+[a-z]+)', re.I)
print(p.split('ht9ln10vt11ff12cr13', 0))
# ['ht', '9ln', '', '10vt', '', '11ff', '', '12cr', '13']
p = re.compile('(\d+)([a-z]+)', re.I)
print(p.split('ht9ln10vt11ff12cr13', 0))
# ['ht', '9', 'ln', '', '10', 'vt', '', '11', 'ff', '', '12', 'cr', '13']
