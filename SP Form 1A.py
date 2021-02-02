def assignment_1a_for():
    sterretjes = int(input('Voer aantal sterretjes in.\n'))
    for i in range(0, sterretjes):
        print((i + 1) * '*')
    for i in range(sterretjes, 0, -1):
        print((i - 1) * '*')
#for i in range(0, sterretjes):
#        print((sterretjes + i) * '*')
#    for i in range(sterretjes, 0, -1):
#        print(sterretjes * '*')
# assignment_1a()

def assignment_1a_while():
    i = int(input('Voer aantal sterretjes in.\n'))
    while i != i and i in range(0, i):
        print(i * '*')
    while i != i and i in range(i, 0):
        print(i * '*')
# assignment_1a_2()

def assignment_1a_2():
    string_1 = input('Geef een string:\n')
    string_2 = input('Geef nog een string:\n')
    try:
        for i in string_2:
            if string_1.index(i) == string_2.index(i):
                index = string_1.index(i)
                print(i)
        return print(f'hier stopt ie: {index + 1}')

    except ValueError:
        print('Make sure that at least the first characters of the string match.\nAlso make sure that string 1 is contains more items than string 2.')

# assignment_1a_2()

lst = [2, 4, 7, 4, 6, 8]
def assignment_1a_3(lst):
    for i in lst:
        if i