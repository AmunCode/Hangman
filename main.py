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


def update(word):

    strikes = 0 # <-- Do I need this? 7#07_73|\|

    word_display = []
 
    correct_letters = []
 
    wrong_letters = []
 
    hangman_imgs = ['A','B','C','D','E','F']
    '''To be replaced with actual images provided by Greg'''
   
def display(correct_letters,wrong_letters,word):
  print(hangman_imgs([len(wrong_letters)]) +  print("Wrong:")
  
  for w in wrong_letters:
    print(guess, end='')


while strikes < 6:
  game_over = False

  blanks = "_" * len(secret_word)

  for s in range(len(secret_word)):
  if guess[s] in correct_letters:  
    blanks = blanks[:s] + secretWord[s] + blanks[s+1:]
    else: 
      hangman_imgs = hangman_imgs[+1]
      strikes += 1
      wrong_letters = guess.append()
      print("Incorrect.")
      print(hangman_imgs)
  
  for b in blanks: 
    print(letter, end=' ')
    print()
    '''Not so sure about this section'''
    
  if strikes == 6:
    game_over = True
    print ("GAME OVER")
  elif blanks == 0:
    print("VICTORY!") 
  elif blanks == 0 and strikes == 0:
    print("VICTORY! You're one smart cookie!") 


# 7#07_73|\|