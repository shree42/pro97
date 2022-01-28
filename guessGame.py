import random

number=random.randint(1,9)
chances=0
while chances<5:
    no=int(input("Guess a random number between 1 & 9"))
    if(no==number):
        print("You guessed it right!")
        break
    elif(no<number):
        print("Oops too low , guess higher")
    else:
        print("Oops too high , guess lower ")
    chances+=1
    if(chances==5):
        print("You are out of chances,number is",number)
