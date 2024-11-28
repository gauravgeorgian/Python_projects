import random

print('You have to Enter the number limit from which you have to guess the random number')
a=int(input("Enter the first number=" ))
b=int(input('Enter the last number='))

number=random.randint(a,b)

guesses=b/4

guess=0
while True:
    guess = int(input('Enter your guess='))
    if guess==number and guesses!=0:
        print("You Won baby")
        break
    elif guess>number and guesses!=0:
        print("Oh this is the Greatest of All time. So, Try Smaller")
        guesses-=1

    elif guess<number and guesses!=0:
        print("Try bigger one")
        guesses-=1

    else:
        print("thoo! laanat hai tere pe LOOSER")
        break



