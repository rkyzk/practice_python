import random
from alphabet import alphabet

words = []
with open('words.py') as f: 
    words = f.read().splitlines()
while True:
    word = random.choice(words)
    answer = ""
    string = ""
    for n in range(len(word)):
        string = string + "_ "
    print(string)
    print("Let's play hangman. Hangman has 6 body parts: a head, \
        a torso, two arms and two legs, so you can get wrong up to 5 times. \
        You lose at 6th time")
    num_wrong_guess = 0     
    chars = [*word]
    guessed_letters = []

    while answer != word:
        letter = input("Type a letter: ").lower()
        if letter not in alphabet:
            print("You need to type in a letter") 
            continue 
        if letter in word:
            ind_list = [idx for idx, item in enumerate(word) if letter in item]
            for n in range(len(ind_list)):
                val = (len(chars) - (ind_list[n] + 1))
                if val != 0:
                    string = string[:ind_list[n] * 2] + letter + " " + string[-val * 2:]
                else:
                    string = string[:ind_list[n] * 2] + letter + " "    
            print(string)        
            answer = string.replace(" ", "")
            if answer == word:
                print(f"You got it right! '{answer}' is the answer \
                    Play a new game") 
                break
        else: 
            num_wrong_guess += 1
            if num_wrong_guess == 6:
                print(f"Gameover!  The word was '{word}' \
                    Play a new game")
                break
            guessed_letters.append(letter)
            print(f"You got {num_wrong_guess} times wrong / 5. \
                You already guessed '{guessed_letters}")
        

