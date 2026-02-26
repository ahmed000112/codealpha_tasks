import random
words= ["python","java","coding","program","computer"]
secret_word=random.choice(words)
guessed_letters=[]
max_attempts=6
wrong_attempts=0
display_word=["_"]*len(secret_word)
print("Welcome to Hangman Game!")
print("You have 6 incorrect guesses allowed.")
while wrong_attempts<max_attempts and "_" in display_word:
    print("\nword:","".join(display_word))
    print("Remaining attempts:",max_attempts-wrong_attempts) 
    guess=input("Guess a letter:").lower()
    if len(guess)!=1 or not guess.isalpha():
        print("please enter only one alphabet letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue
    guessed_letters.append(guess)
    if guess in secret_word:
        print("Good guess!")
        for index in range(len(secret_word)):
            if secret_word[index]==guess:
                display_word[index]=guess
    else:
        wrong_attempts+=1
        print("Wrong guess!")
if"_" not in display_word:
    print("\nCongratulations! You guessed the word:",secret_word)
else:
    print("\nGame over! The word is :",secret_word)
    

