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


#Thot 
guess = input('Please guess a letter:').upper()
if len(guess) == 1 and guess.isalpha():
  if guess in guessed_letters:
    print('You already guessed this letter'), guess)
elif guess not in word:
  print(guess, 'is not on word.')
  tries -= 1
  guessed_letters.append(guess)
else:
  print('Good Job!,',guess,'is in the word!')
  guessed_ letters.append(guess)
  word_list = list(word_completion)
indices =[i for i in enumerate(word)]if letter == guess]
for index in indices:
  word_list[index] = guess
  word_completion = "".join(word_list)
  if "_" not in word_ccompletion:
    guessed = True
elif len(guess) == len(word) and guess.isalpha():
 if guess in guessed_words:
   print'(You already guessed the word!', guess)
 elif guess != word:
   print(guess, 'is not the word!')
   tries -= 1
   guessed_words.append(guess)
 else:
   guessed = True
   word_completion = word
else:
  print('Not a valid guess!')
