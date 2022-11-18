import random

score_comp = 0
score_user = 0
options = ["Rock", "Scissors", "Paper"]

while True:
    num = random.randrange(3)
    print("Select rock(r), scissors(s), paper(p) or Q to quit.")
    choice_user = input("Your choice: ").lower()

    if choice_user not in ["r", "s", "p", "q"]:
        print('Enter only r, s, p or q')
        continue

    print(f"Computer chose: {options[num]}")    

    if choice_user == "r":
        if options[num] == "Rock":
            print("We tied.")
        elif options[num] == "Scissors":
            print("You won.")
            score_user += 1
        else:
            print("I won.")
            score_comp += 1

    elif choice_user == "s":
        if options[num] == "Scissors":
            print("We tied.")
        elif options[num] == "Paper":
            print("You won.")
            score_user += 1
        else:
            print("I won.")
            score_comp += 1

    elif choice_user == "p":
        if options[num] == "paper":
            print("We tied.")
        elif options[num] == "Rock":
            print("You won.")
            score_user += 1
        else:
            print("I won.")
            score_comp += 1
    
    else:
        print(f"We'll end the game.  You scored: {score_user}. \
            I scored: {score_comp}") 
        break

print("Bye!")