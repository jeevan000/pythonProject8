def generate_random_code():
    from random import randint
    code_answer = [] # Create list to insert randomly chosen numbers into
    for i in range(0, 4): #----->  loop to utilize random method 4 times
        number = str(randint(0, 5)) #-----> Pick a random number between 0 - 3 to signify colours
        code_answer.append(number)
    return code_answer
    # generate_random_code()
def guess_code():
    code_answer = generate_random_code()
    print(code_answer)
    input_code = list(input("Enter your guess:"))

    if input_code == code_answer: #------ compare input to auto-generated code
        print("Congratulations, you've guessed the code!")
    else:
        feedback()
        print(input_code)
        return input_code
guess_code()
def feedback(): # work in progress
    # generate_random_code()
    check = guess_code()
    for i in check:
        print(i)



# Randomize feedback