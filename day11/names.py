from name_function import get_formatted_name

print('input "q" at any time to quit')
while True:
    first = input('\n Please give me first name: ')
    if first == 'q':
        break
    last = input('\b Please give me you last name: ')
    if last == 'q':
        break
    full_name = get_formatted_name(first=first, last=last)
    print(f"\t the neatly name:{full_name}")
