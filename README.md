# HANGMAN
### Video Demo:  https://www.youtube.com/watch?v=NcOIOGt3GYw
### Description: A hangman game written in python that you can easily play in linux terminal

### Files:
1. `hangman.py` (Main program is written in this file and this is the file that needs to be executed)
2. `english_words.txt` (Text file containing line separated words of english language. This is the file used by the program to randomly pick out a word everytime you run the main program)
3. `README.md`

### Structure of the Game
Running the hangman.py file starts the program. First and foremost the program will print out name of the game, author and rules of the game for the player. Secondly the program will pick a random word from almost 260000+ english words in the text file for the player to guess. Player will have 9 tries to guess alphabets of english language to get to the word. If the player gets the complete word before making 9 mistakes they win otherwise they lose.

### Guts of the program
Main piece of the program in hangman.py is a sophisticated while loop with a multiple conditionals that make the program go on until either the player wins (All letters of the word guessed correctly) or loses (remaining tries become zero). Theres a function hangman_image(n) that makes sure the correct image is to be printed depending on the number of tries remaining.

### User inputs
The input to the game can only be single alphabetic characters and that is taken care of in the while loop inside which the input function lives. The program will throw errors and request input again if following inputs go in:
1. numbers for example 1,2,3,135,624,.12
2. multiple alphabets for example afd, agfsg, ahkoold, ad
3. empty string
All such inputs are rejected by the program and user is prompted to re-enter input. Program does not break with invalid inputs

The hangman program is case insensitive to input alphabet and takes care of lower and upper case letters in similar fashion. There is also a graphic for the hangman that prints in the terminal everytime player makes a guess. You have to save the the man from getting hanged and the graphic gives you additional motivation to think harder if your number of remaining tries is low.

### Some Challenges
Major challenge was dealing with hiding the word and only revealing the letters which have been guessed correctly at a given point in time. Since strings are immutable it was not possible. After a lot of deliberation and understanding that only one word needs to be dealt with by my program at a time i decided to break the string down into a list of characters. Lists are mutable and this opened all locked doors for me. I was able to hide and reveal different letters of the word in my list structure easily and at time of printing I could just " ".join(result)

Thinking about how to print the image of hangman was a though provoking process because it was not straightforward. As soon as i thought about linking the image to n variable which is number of tries left I developed a strategy for the image function quickly.

### Enjoy the game!