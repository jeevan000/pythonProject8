# Setup Mastermind
Divide game modes into modules:
module 1: base functions; code generator, guess
module 2: game rules; max amount of tries, range of numbers, length of row on board. 
module 3: game modes; AI vs player, player vs AI
Module 4: strategies

define function generate Code:
  pick 4 numbers from range from 0-5 with random number generator
  combine numbers into single code
  save code
  
define function guess   
  Ask player for input code
  Save input code
  Set limit to 10 attempts
  
define function to check guess using input code
  if input code equals random generated code
    tell player that they've successfully guessed the code.
  if not: call function which gives feedback

define function to give feedback using input and randomly generated code; take into account the maximum amount of feedback pins [4]
  loop through the input code to check if any of the numbers correspond with any of the generated code taking into account the correct and incorrect positions.
  if so: return 2 for each corresponding number with correct position.
  if not entirely correct: return 1 for each corresponding number with incorrect position.
  if entirely incorrect: return 0 for each completely incorrect number.

Sources:Boss, R. (2021, 19 januari). HU Structured Programming - Mastermind. Youtube. https://www.youtube.com/watch?v=rSzX2TtjvHA&feature=youtu.be
       :Kooi, B. (2005). YET ANOTHER MASTERMIND STRATEGY. ICGA Journal, 28(1), 13–20. https://doi.org/10.3233/icg-2005-28105

Libraries used: 
random

