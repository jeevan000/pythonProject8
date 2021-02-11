import random
import itertools
# valid_chars = ['0', '1', '2', '3', '4', '5']
# all_combinations = (list(itertools.product(valid_chars, repeat=4)))
# all_combinations = [list(i) for i in all_combinations]
# print(all_combinations[1295])
def generate_all_code():
    all_possibilities = []
    for i in range(0, 6):
        for j in range(0, 6):
            for x in range(0, 6):
                for y in range(0, 6):
                    all_possibilities.append(str(i) + str(j) + str(x) + str(y))
    print(range(len(all_possibilities[0])))
    code_answer = [all_possibilities[random.randint(0, len(all_possibilities))]]
    # print(code_answer)
    return all_possibilities, code_answer

    # code_answer = [] # Create list to insert all possibilities into
    #
    # for i in range(0, 4): #----->  loop to utilize random method 4 times
    #     number = str(random.randint(0, 5)) #-----> Pick a random number between 0 - 5 to signify colours
    #     code_answer.append(number)
    # print(code_answer)
    # code_answer = list(''.join(code_answer))
    # print(range(len(code_answer[0])))
    # return code_answer
# generate_random_code()

guess = ['3223']
def check_guess(code_answer, player_input):
    # input_code = list(input("Enter your guess:"))
    # print(input_code)
    all_possibilities = generate_all_code()
    code_answer = all_possibilities[random.randint(0, len(all_possibilities))]
    print(code_answer)
    if code_answer == guess: #------ compare input to auto-generated code
        print("Congratulations, you've guessed the code!")
    else: #>>>>>>>>>>>>>>> This else statement provides feedback for wrong answers
        # colour_numbers = ['0', '1', '2', '3', '4', '5']

        black, white = 0, 0

        """ Create two more lists to store the individual numbers of the code_answer and the guess in to compare
        step by step if the codes are aligned and another list to insert the net amount of black and white pins into."""
        list_guess = []
        list_code_answer = []
        result = []
        for i in range(len(all_possibilities[0])):


            if guess[i][i] == code_answer[i][i]:
                black += 1
            else:
                list_guess.append(guess[i])
                list_code_answer.append(code_answer[i])
        # print(list_guess)
        # print(list_code_answer)

        # for i in all_possibilities:
        # all_possibilities = (list(itertools.product(colour_numbers, repeat=4)))
        # all_possibilities = [list(i) for i in all_possibilities]
        # print(all_possibilities)
        # for i in all_possibilities
        #     if guess.index(i) == code_answer.index(i):
        #         black += 1
        #     else:
        #         print(black)
        # print('wrong!')
check_guess(generate_all_code(), guess)


# if statement voor pinkleuren met for loop


