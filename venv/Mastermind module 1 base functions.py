import random
def generate_all_code():
    all_possibilities = []
    for i in range(0, 6):
        for j in range(0, 6):
            for x in range(0, 6):
                for y in range(0, 6):
                    all_possibilities.append(str(i) + str(j) + str(x) + str(y))
    secret = all_possibilities[random.randint(0, len(all_possibilities))]
    return secret

guess = '3223'
def check_guess(secret, guess):
    if secret == guess: #------ compare input to auto-generated code
        print("Congratulations, you've guessed the code!")
    else: #>>>>>>>>>>>>>>> This else statement provides feedback for wrong answers
        """ Creates more lists to store the individual numbers of the secret code and the guess into to compare
        step by step if the codes are aligned and to insert the net amount of black and white pins and their indices into."""
        black_list = []
        black_list_index = []
        white_list = []
        white_list_index = []
        result = [0, 0] #------> This is the ultimate result: the first number = black pins, the second number = white
        # pins
        for i in range(len(guess)): #-----> check whether the numbers of the two codes are similar and in the same spot
            if guess[i] == secret[i]:
                result[0] += 1
                black_list.append(guess[i])
                black_list_index.append(i)
        print(f'black_list: {black_list}')
        print(f'blacklistindex: {black_list_index}')
        for i in range(len(guess)): #----> check if the numbers are not a black pin and check if they're in the code
            # but not in the same spot (does not work yet)
            if guess[i] not in black_list and guess[i] in secret:
                result[1] += 1
                white_list.append(guess[i])
                white_list_index.append(i)
        print(f'whitelist: {white_list}')
        print(f'whitelistindex: {white_list_index}')


        return result
print(check_guess(generate_all_code(), guess))
