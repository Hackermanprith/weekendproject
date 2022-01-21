
"""
Hangman by Prithwish Mukherjee 
Google Dev Account: https://developers.google.com/profile/u/pmdev
Replit Account: https://replit.com/@PrithwishMukher
Devto: https://dev.to/dashboard

"""
"""
I am not completing the word list right now please do it your self as I am quite lazy.
"""
import random
from termcolor import colored,cprint
from pyfiglet import Figlet
import string

wordlist_0 = ["hit","bit","kit"]
wordlist_3 = ["hi","lol","bruh"]
wordlist_2 = ["bruhh","curhh","muhh"]
#base vars for font
f = Figlet(font='banner3-D')
print(colored(f.renderText("Welcome to PyHangman"),'green'))

#setting a random level for kids
def get_random_word(difficulty_level):
    if difficulty_level == "1":
        word = random.choice(wordlist_0)
    elif difficulty_level == "2":
        word = random.choice(wordlist_2) 
    elif difficulty_level == "3":
        word = random.choice(wordlist_3)
        
    return word.upper()


def hangman_main_play(word):
    #creating base var
    used_letters = set() 
    word_letters = set(word)
    #all english alphabets in english
    alphabet = set(string.ascii_uppercase)
    
    
    #lives
    lives = 0
    for i in range(0,len(word)):
        lives +=1
    
    #main gameplay
    while len(word_letters) > 0 and lives > 0:
        print(" ")
        
        print("You have "+ str(lives) +" left",'green')
        print(" ")
        
        print("You have used this letter ",''.join(used_letters))
        print(" ")
        #if else
        word_list = [letter if letter in used_letters else " - " for letter in word]
        print("current word:",''.join(word_list))
        print("")
        user_inp_letter = input("Enter the gussed letter").upper()
        if user_inp_letter in alphabet - used_letters:
            #adding the input if it is in alphabets and also not in used letters
            used_letters.add(user_inp_letter)
            if user_inp_letter in word_letters:
                #removing the inputed letter from the set of word
                word_letters.remove(user_inp_letter)
                print('')
            else:
                #else live -1
                lives -= 1
                print(user_inp_letter + " is not in the word")
        elif user_inp_letter in used_letters:
            #else if in used letter 
            print(" ")
            lives -= 1
            print("You already guessed that letter")
            #wining and loosing set
        if lives == 0:
            print("You lost, you are such a looser")
        else:
            print("Yay you have won , You ar really good at the game",'purple')    
def welcome():
    cprint("              Welcome to Hangman by Prithwish Mukherjee  ", 'red')
    cprint('        You will have to guess the name of the youtuber , For each correct','yellow')
    cprint('        you will get another extra life and wrong name guess will lead to ','green')
    cprint('        1 life loss, You will also be given hints,As we all know you are a noob','blue')
    cprint('PS: DO NOT ENTER SPACES FOR EXAMPLE IF YOUT GUESS IS TECHNO GAMERZ ENTER TECHNOGAMERZ','magenta')

user_inp_difficulty = input("Enter your difficulty level")

hangman_main_play(get_random_word(user_inp_difficulty))  

