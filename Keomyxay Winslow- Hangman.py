import random
"""
This is a guide of how to make hangman.

1. Make a word bank of 10 items.
2. Select a random item to guess.
3. Take in a letter and add it to a list of letters_guessed.
4. Hide and reveal letters.
5. Create win and lose conditions.
"""


# Hangman
print("This is Hangman....")
guess = 10
guesses_Taken = 0
letter_used = []
letter_guessed = []
print("This is a political word bank...")
print("You have 10 guesses.")
word_bank = ["Republican", "Government Shutdown", "Presidency", "Parris Island", "Senator",
 "Defectors", "Rocket Man", "North Korea", "Congressman", "West Point"]


strOne = random.choice(word_bank)

guess = ""
while guess != "quit":
    output = []
    # Builds the output
    for letter in strOne:
        if letter in letter_guessed:
            output.append(letter)
        else:
            output.append("*")
    # Display output
    # print(output)
    print(''.join(output))

    print("Guess a letter.")
    guess = input('>_')
    letter_guessed.append(guess)

# for num in range(len(word_bank)):
#    item = word_bank[num]
#   print ("The item at index %d is %s" % (num, item))
