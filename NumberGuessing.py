import random
import math

low = int(input("Enter the lower bound= " ))
high = int(input("Enter the upper bound= "))

x= random.randint(low,high)
print("\n\tYou have only ", round(math.log(high-low+1,2)), "chance to guess the intger! ")

count = 0

while count< math.log(high-low+1,2):
    count+=1

    guess = int(input("Guess a number: "))

    if x == guess:
        print("Congratulation you have did it in", count, "try :)" )
        break
    elif x>guess:
        print("You guessed to small :(")
    elif x<guess:
        print("You guessed to high :(")
if count >math.log(high-low+1,2):
    print("\n The Number is %d " %x)
    print("Better Luck Next Time! ")