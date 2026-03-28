Project Title
Hangman Game – Console Based Python Project


Objective of the Project
The objective of this project is to design and implement a simple text-based Hangman game using Python.
The project aims to help students understand and apply basic programming concepts such as loops, conditions, lists, strings, and user input/output.


Project Description
The Hangman game is a word-guessing game where the computer randomly selects a word from a predefined list.
The player tries to guess the word by entering one letter at a time through the console.
The word is initially hidden using underscores (_)
The player has 6 incorrect attempts
Correct guesses reveal the letters in the word
Incorrect guesses reduce the remaining attempts
The game ends when the word is guessed correctly or all attempts are used
This project is completely console-based and does not use any graphical user interface (GUI).


Technologies Used
Programming Language: Python
Execution Environment: Console / Terminal


How the Game Works (Step-by-Step)
The program starts and displays a welcome message.
A random word is selected from a predefined list.
The word is shown as underscores (_) representing hidden letters.
The user enters one letter at a time through the keyboard.
If the letter exists in the word, it is revealed.
If the letter does not exist, the attempt count decreases.
The game ends when:
The user guesses the full word (Win), or
The user uses all 6 incorrect attempts (Lose).


Sample Console Input and Output
Welcome to the Hangman Game!
You have 6 incorrect guesses allowed.
Word: _ _ _ _ _
Remaining attempts: 6
Guess a letter: a
Good guess!
Word: a _ _ _ _
Remaining attempts: 6
Guess a letter: x
Wrong guess!
Remaining attempts: 5


How to Run the Project
Install Python on your system.
Save the program file as hangman.py.
Open Command Prompt / Terminal.
Navigate to the project folder.
Run the command:
python hangman.py



Limitations
Only single-player mode
Fixed number of words
Console-based interface only



Conclusion
This project successfully implements a text-based Hangman game using Python.
It fulfills all the  project requirements and demonstrates the practical use of basic programming concepts.


Future Enhancements
Add more words
Add difficulty levels
Improve user messages
Convert to GUI or web version
