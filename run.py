import random
from alphabet import alphabet

words = []
with open('words.py') as f: 
    words = f.read().splitlines()

word = random.choice(words)
answer = ""
string = ""
for n in range(len(word)):
    string = string + "_ "
print(string)
print("Let's play hangman. Hangman has 6 body parts: a head, \
    a torso, two arms and two legs, so you lose when you get 6 times wrong.")
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
    else: 
        num_wrong_guess += 1
        if num_wrong_guess == 6:
            print(f"Gameover!  The word was '{word}'")
            break
        guessed_letters.append(letter)
        print(f"You got {num_wrong_guess} times wrong / 5. \
            You already guessed '{guessed_letters}")
        

print(f"You got it right! '{answer}' is the answer") 