import random
targetnumber = random.randint(1,100)
attemptnumber = 0
guess = 0
print("Hii.. wllcome to my game: ")
print("press 1-100 any number i can find it :")
while guess != targetnumber:
    guess = int(input("re-enter the guessnumber:"))
    attemptnumber+=1
    if guess<targetnumber:
        print("it's too low...")
    elif 100>guess>targetnumber:
        print("it's too high...")
    elif guess == targetnumber:
        print(f"congratulation.. you can find it {attemptnumber} attempt..")
    else:
        print("you can enter out of the range number...")
