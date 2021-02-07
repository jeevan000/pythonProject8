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
def assignment_1a_3_1(lst, number):
    count = 0
    for i in lst:
        if i == number:
            count += 1
    print(count)
def assignment_1a_3_2(lst):
    for i in lst:
        diff = lst[i+1] - lst[i]
        return print(diff)
# assignment_1a_3_2(lst)

word = 'sdsa'
def assignment_1a_4():
    if word == word[::-1]:
        return True
    return False

def assignment_1a_5(lst):
    lst_sorted = []
    for i in lst:
        lst_sorted.append(i)
    switch = True
    while switch:
        switch = False
        for i in range(len(lst_sorted) - 1):
            if lst_sorted[i] > lst_sorted[i + 1]:
                lst_sorted[i], lst_sorted[i + 1] = lst_sorted[i + 1], lst_sorted[i]
                print(lst_sorted)
                switch = True
    return lst_sorted

def assignment_1a_6(lst):
    total = sum(lst)
    indices = len(lst)
    average = total / indices
    return average

def assignment_1a_7():
    from random import randint
    input_number = int(input('Voer hier een getal in als bereik:\n'))
    number = randint(0, input_number)
    while True:
        guess = int(input('Raad het getal:\n'))
        if input_number == number:
            print('Goed!')
        else:
            print('Fout!')

def assignment_1a_8():
    with open("compressie", "r") as textfile:
        text = textfile.readlines()
        for i in text:
            i.strip()
            print(i)
        textfile.close()
# assignment_1a_8()
ch = '10101000'
# def assignment_1a_9(ch, n):

# def caesar: string alfabet indexen optellen

# def fizzbuzz: modulo 3 modulo 5 modulo 3 en 5