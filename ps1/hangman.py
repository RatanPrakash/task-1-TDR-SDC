# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
from ast import Try
from pickle import FALSE
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    x = True
    for letter in secret_word:
      if letter not in letters_guessed:
        x = False
        break
    return x
        

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    outList = [' _ '] * len(secret_word)
    for ltr in letters_guessed:
      ind = 0
      for letter in secret_word:
        if ltr == letter:
          outList[ind] = ltr
        ind += 1

    retStr = ''.join(outList)
    return retStr


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    st = ""
    for lettr in string.ascii_lowercase:
      if lettr not in letters_guessed:
        st += lettr
      
    return st
     
  
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    guessed = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    while guesses > 0:
      if is_word_guessed(secret_word, guessed):
        print("Congratulations! You won the game.")
        print(get_guessed_word(secret_word, guessed))
        print("Your score is: ", guesses*len(set(secret_word)) )
        break

      print("-----------------------------------------------------------------------------------")
      print("The word to be guessed is ",len(secret_word), "letters long")
      print(get_guessed_word(secret_word, guessed))
      print("You now have ", guesses, "no. of guesses to guess the word.")
      print("Remaining letters are: ", get_available_letters(guessed))
      Warns = 0
      while Warns <= 3:
        guess = input("Enter a letter : ")
        guess.lower()
        if guess.isalpha() and len(guess) == 1 and guess in get_available_letters(guessed):
          break
        elif guess not in get_available_letters(guessed):
          print("That letter is already guessed. Choose a letter only from the available ones.")
          print("You've been warned.", 3 - Warns," warnings left.")
          Warns += 1
        else:
          print("Enter a valid and a single char.")
          Warns += 1
      else:
        print("You lost 1 guess.")
        guesses -= 1
        continue

      if guess in secret_word and guess in get_available_letters(guessed):
        print("Good guess, keep going.")
      elif guess not in secret_word and guess in get_available_letters(guessed) and guess in vowels:
        print("Oops, try another letter. Since that was a vowel you LOST 2 Guesses.")
        guesses -= 2
      else:
        print("Oops! Try another letter.")
        guesses -= 1

      guessed += guess
    #loop ends
    if guesses == 0 and is_word_guessed(secret_word, guessed):
      print("Congratulations! You won the game.")
      print("-----------------------------------------------------------------------------------")
    elif guesses == 0:
      print("We're sorry, You lost the game. \n The word was: ", secret_word)
      print("-----------------------------------------------------------------------------------")



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word = my_word.replace(" ", "")
    if len(my_word) != len(other_word):
      return False
    else:
      index = 0
      ret = True
      for i in my_word:
        if i == "_":
          index += 1
          continue
        elif i != other_word[index]:
          ret = False
          index += 1
          break
        else:
            index += 1
      return(ret)

    
def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matches = []
    for word in wordlist:
      if match_with_gaps(my_word, word):
        matches.append(word)
    
    return matches



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses = 6
    guessed = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    while guesses > 0:
      if is_word_guessed(secret_word, guessed):
        print("Congratulations! You won the game.")
        print(get_guessed_word(secret_word, guessed))
        print("Your score is: ", guesses*len(set(secret_word)) )
        break

      print("-----------------------------------------------------------------------------------")
      print("The word to be guessed is ",len(secret_word), "letters long")
      print(get_guessed_word(secret_word, guessed))
      print("You now have ", guesses, "no. of guesses to guess the word.")
      print("Remaining letters are: ", get_available_letters(guessed))
      Warns = 0
      while Warns <= 3:
        guess = input("Enter a letter : ")
        guess.lower()
        if guess.isalpha() and len(guess) == 1 and guess in get_available_letters(guessed):
          break
        elif guess not in get_available_letters(guessed) and guess.isalpha():
          print("That letter is already guessed. Choose a letter only from the available ones.")
          print("You've been warned.", 3 - Warns," warnings left.")
          Warns += 1
        elif guess == "*":
          print(show_possible_matches(get_guessed_word(secret_word, guessed)))
        
        else:
          print("Enter a valid and a single char.")
          Warns += 1
      else:
        print("You lost 1 guess.")
        guesses -= 1
        continue

      if guess in secret_word and guess in get_available_letters(guessed):
        print("Good guess, keep going.")
      elif guess not in secret_word and guess in get_available_letters(guessed) and guess in vowels:
        print("Oops, try another letter. Since that was a vowel you LOST 2 Guesses.")
        guesses -= 2
      else:
        print("Oops! Try another letter.")
        guesses -= 1

      guessed += guess
    #loop ends
    if guesses == 0 and is_word_guessed(secret_word, guessed):
      print("Congratulations! You won the game.")
      print("-----------------------------------------------------------------------------------")
    elif guesses == 0:
      print("We're sorry, You lost the game. \n The word was: ", secret_word)
      print("-----------------------------------------------------------------------------------")




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
#     # pass

#     # To test part 2, comment out the pass line above and
#     # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

# secret_word = choose_word(wordlist)
# hangman("lolum")


###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
