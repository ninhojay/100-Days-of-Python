import random

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| 
                    __/ |                      
                   |___/    '''
print(logo)

stages = ['''  
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel", "martin", "persist", "patience", "determination"]

# TODO-1: Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
lives = 6
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Initialize the placeholder with underscores for each letter in the chosen word
placeholder = "_" * word_length

# Display the initial placeholder
print(f"Word to guess: {placeholder}")

game_on = True
correct_letters = []

while game_on:
    print(f"You have: {lives}/6 Lives left ")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")
        continue

    correct_letters.append(guess)

    display = ""

    # Update the display placeholder with correct guesses
    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    # Check if the guess is in the chosen word
    if guess not in chosen_word:
        lives -= 1
        print(f"You've guessed {guess}, which is not in the word. You lost a life")
        if lives == 0:
            game_on = False
            the_end = input("Well done, hope you enjoyed the game? If yes, press 1, if no press 0: ").strip()
            if the_end == '1':
                print(f"YOU LOSE. The correct word was: {chosen_word}")
            elif the_end == '0':
                print(f"Oops, thanks for playing by the way, the correct word was: {chosen_word}")
    else:
        if "_" not in display:
            game_on = False
            print("You win! Congratulations")

    print(stages[lives])
    print(f"Word to guess: {chosen_word}")
