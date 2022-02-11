# List of guesses
guesses = []

# Ask you user to guess a letter and store it in guesses list
userinput: bool = True
while userinput:
    letter = input("Guess A Letter ")
    if not letter in guesses:
        confirmed = input("Are you Sure? type 'YES' to Confirm, 'NO' to select a different letter ").upper()
        if confirmed == 'YES':
            userinput: bool = False
            guesses.append(letter)
    else:
        print('That letter has already guessed. Try another one')

print(guesses)
