# list with hangman ASCII art. Can be traversed by indices.
hangman_imgs = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
# Thot 4
guesses = []                                        # List of Guesses

# Ask user to guess a letter and store it in guesses list
userinput: bool = True
while userinput:
    letter = input("Guess A Letter ")
    if letter.isalpha():                            # Validate character is a letter
        if len(letter) == 1:                        # Validate user only entered 1 Letter
            if not letter in guesses:               # Check if Letter has already been guessed
                confirm_guess = input("Are you Sure? type 'YES' to Confirm, 'NO' to guess a different letter ").upper()
                if confirm_guess == 'YES':
                    userinput: bool = False
                    guesses.append(letter)          # Add Letter to the guesses List
            else:
                print('That letter has already guessed. Try another one')
        else:
            print('You can only guess ONE letter at a time')
    else:
        print('Invalid Character, You can only guess a Letter')
