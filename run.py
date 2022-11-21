import random

words = []
with open('words.py') as f: 
    words = f.read().splitlines()

word = "hammer"
print(word)
answer = ""
string = ""

while answer != word:
    letter = input("Type a letter: ")
    if letter in word:
        ind_list = [idx for idx, item in enumerate(word) if letter in item]
        print(ind_list)
    
        for i in range(ind_list[0]):
            string = string + "_ " 
            
        string = string + letter

        for i in range(len(word) - ind_list[-1] - 1):
            string = string + "_ "
        print(string)

    

