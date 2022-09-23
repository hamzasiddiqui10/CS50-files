import numpy as np

# Open the text file with all the words
with open('english_words.txt', 'r') as open_file:
    all_text = open_file.read()

mylist = all_text.split('\n')

# Print the Title and Rules of the game
print(f"""
-----------------------
-----------------------
-- CS50x - Project
-----------------------
-----------------------
-- >> H-A-N-G-M-A-N <<
-----------------------
-- by Hamza A. Siddiqui
-----------------------

-- Rules:
-- 1. You will get 9 guesses.
-- 2. You will guess letters of the alphabet.
-- 3. If you guess correctly your guess letter will show up in the display otherwise your tries will be deducted.
-- Total words available = {len(mylist)}
-----------------------
-----------------------
""")


def main():

    # Select a random word from english_words.txt file
    idx = np.random.randint(0, len(mylist))
    word = mylist[idx]

    unique_letters = set(word.upper())

    result = []
    for i in word:
        result.append("_")

    guessed_letters = set()

    n=9

    print("""--------------------------------------------\n--------------------------------------------""")
    print('\nGuessed Letters: ' + ", ".join(guessed_letters))
    print("Tries Remaining: " + str(n))
    print(" ".join(result))

    # Run game until the word is not completely guessed by player
    while not set(word).issubset(guessed_letters):
        print("""--------------------------------------------\n--------------------------------------------""")

        # Get the guess letter and make sure it is alphabet and has length 1
        g = '100'
        while(not (g.isalpha() and len(g) == 1)):
            g = input("Guess your alphabet: ").strip().upper()
            print("Error: Please enter a single letter of alphabet")

        # If g is a new guess
        if g not in guessed_letters:
            # Add g to guessed letters
            guessed_letters.add(g)

            # If g is a letter in WORD then make it appear in the guessed word
            if g in word:
                print("\n------CORRECT!------")
                indexes = [idx for idx, x in enumerate(word) if x==g]
                for i in indexes:
                    result[i] = g

            else:
                n -= 1
                print("\n-----INCORRECT!-----")

        else:
            print("-You already guessed this letter")

        print(hangman_image(n))

        # If player runs out of tries game is over.
        if n==0:
            print("\n---------------------------------------\n** GAME OVER. YOU LOSE **" + " Word was " + word + "\n--------------------------------------")
            break


        print('Guessed Letters: ' + ", ".join(guessed_letters))
        print("Tries Remaining: " + str(n))
        print(" ".join(result))

        # Win condition
        if set(word).issubset(guessed_letters):
            print("\n--------------------------------------------\n** YOU WIN **" + " Word was " + word + "\n--------------------------------------------")


# Funtion for creating the hangman at every value of n i.e. tries left
def hangman_image(n):

    lives = [
    """
        X_______
        |     |
        |     O ----{Hanged!}
        |    \|/
        |     |
        |    / \\
        |
      |''''''''''''|
      |____________|
    """,
    """
        X_______
        |
        |     O
        |    \|/
        |     |
        |    / \\
        |
      |''''''''''''|
      |____________|
    """,
    """
        X_______
        |
        |     O
        |    \|/
        |     |
        |    /
        |
      |''''''''''''|
      |____________|
    """,
    """
        X_______
        |
        |     O
        |    \|/
        |     |
        |
        |
      |''''''''''''|
      |____________|
    """,
    """
        X_______
        |
        |     O
        |    \|
        |     |
        |
        |
      |''''''''''''|
      |____________|
    """,
    """
        X_______
        |
        |     O
        |     |
        |     |
        |
        |
      |''''''''''''|
      |____________|
    """,
    """
        X_______
        |
        |     O
        |
        |
        |
        |
      |''''''''''''|
      |____________|
    """,
    """
        X_______
        |
        |
        |
        |
        |
        |
      |''''''''''''|
      |____________|
    """,
    """







      |''''''''''''|
      |____________|
    """,
    """
    """
    ]

    return lives[n]


main()