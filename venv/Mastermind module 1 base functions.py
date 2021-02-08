"""Ik ga mijn feedback noteren met aanhalingstekens zoals hier te zien"""

"""
import random <---"""

def generate_random_code(): """Is het niet een beter idee om een lijst te maken met alle opties en daar een key uit te halen?"""
    from random import randint """Een alternatief is dit weg halen en neerzetten als hier boven. ^^"""
    # code_answer = [] # Create list to insert randomly chosen numbers into
    for i in range(0, 4): #----->  loop to utilize random method 4 times
        number = str(randint(0, 5)) #-----> Pick a random number between 0 - 3 to signify colours
"""Goede notities in de bovenstaande zinnen, het pijltje maakt het extra duidelijk"""
        # code_answer.append(number)
    type(number)
    return print(number) """Al met al een vrij grote fuctie om 1 random getal te krijgen"""

    # return code_answer
    # generate_random_code()
    
def guess_code("""Misschien dingen hier zetten?"""): """Gebruik dit als functie die elke keer alleen de code_answer checkt zodat je het kan blijven hergebruiken."""
    code_answer = generate_random_code() """Dit NIET doen aangezien je nu elke keer als je gues_code runt een nieuwe code_answer aan maakt."""
    print(code_answer)
    input_code = (input("Enter your guess:"))"""Als je deze functie ook door je bot wilt laten gebruiken om de code te raden met dit geen input zijn.
    Het lijkt mij verstandiger om input tussen de haakjes bovenaan mee te geven zodat wanneer je zelf raad het een input is en anders wat de bot zegt."""

    if input_code == code_answer: #------ compare input to auto-generated code 
        print("Congratulations, you've guessed the code!")
    """De if statement is correct"""
    else: """Do de feedback in deze functie ipv losse feedback functie aanmaken."""
        # feedback() 
        # print(input_code)
        return input_code """geen juiste return"""
    """Je gebruikt de guess_code enorm als een soort main functie waar je de andere functies ook benoemt ipv de code te raden
       Mijn tip is om als input je gok of de computers gok te geven en dan als output of het correct is of de feedback functie"""

guess_code()
def feedback(): 
    feedback_pins = {black: 0, """Maak hier een variable van"""
                     white: 0}

    # generate_random_code()
    # if statement voor pinkleuren met for loop
    """Is dit niet precies waar de guess_code voor is"""


# Randomize feedback
