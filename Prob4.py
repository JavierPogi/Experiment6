def hangaroo(secretWord):
    print('You are my prisoner.')
    print("Let's play a little game ")
    print('Guess the word that has', len(secretWord), "letters.")
    print('If you guess the word then you may leave. ')
    lettersGuessed = []

    while isWordGuessed(secretWord, lettersGuessed) ==False:
        print('------------')
        print("You haven't used these letters yet:", getAvailableLetters(lettersGuessed))
        guess = str(input('Guess a letter !: ')).lower()
        if guess in secretWord and guess not in lettersGuessed:
        		lettersGuessed.append(guess)
        		print('Nice one! ', getGuessedWord(secretWord, lettersGuessed))
        elif guess in lettersGuessed:
        		print("You did that already!: ", getGuessedWord(secretWord, lettersGuessed))
        elif guess not in secretWord:
        		print("Guess again!: ", getGuessedWord(secretWord, lettersGuessed))
        		lettersGuessed.append(guess)
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print('------------')
        print('You have guessed the word, you are free to go! ')