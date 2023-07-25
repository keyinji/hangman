import random 

words = ["knock","commission", "president", "sample", "listen", "faithful", "hell", "inn", "portion", "investigation", "knee", "limit", "operational", "condition", "manufacturer", "seminar", "preparation", "chapter", "salmon", "privacy", "stamp", "glow", "uniform", "memorial", "kit", "complete", "exact", "presidency", "bomber", "mystery", "discount", "raid", "class"]

computer_choice = random.choice(words)


for x in computer_choice:
    print("_", end=" ")

def hangman(wrong):
    if wrong == 0:
        print("6 tries remaining")
    elif wrong == 1:
        print("5 tries remaining")
    elif wrong == 2:
        print("4 tries remaining")
    elif wrong == 3:
        print("3 tries remaining")
    elif wrong == 4:
        print("2 tries remaining")
    elif wrong == 5:
        print("1 try remaining")
    else:
        print("You lost")

def hangman_correct(correct):
    counter=0 
    right_letters=0
    for char in computer_choice:
        if char in correct:
            print(computer_choice[counter], end=" ")
            right_letters+=1
        else:
            print(" ", end="")
        counter+=1
    return right_letters


def print_lines():
    print("\r")
    for char in computer_choice:
        print("\u203e", end =" ")

length = len(computer_choice)
wrong = 0
guess_index=0
letters_guessed = []
letters_right = 0

while(wrong != 6 and letters_right != length):
    print("\nLetters guessed so far:")
    
    for letter in letters_guessed:
        print(letter, end=" ")
    letter_guessed = input("\nGuess letter: ")

    if(letter_guessed == computer_choice[guess_index]):

        hangman(wrong) 

        guess_index+=1
        letters_guessed.append(letter_guessed) 
        letters_right=hangman_correct(letters_guessed)
        print_lines()

    else:
        wrong+=1
        letters_guessed.append(letter_guessed)
        hangman(wrong)
        letters_right = hangman_correct(letters_guessed)
        print_lines()

print("over")
