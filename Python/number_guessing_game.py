
#Number guessing game
#Built a Number guessing game, in which the user selects a range.
#Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.
#Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses
import random
import math
lower=int(input("Enter lower bound: "))
upper=int(input("Enter upper bound: "))
#generating rendom numbers between upper and lower bound
x=random.randint(lower,upper)
print("\n\t You have only", round(math.log(upper-lower+1,2)),"chances to guess the integer")
#initialize the number of guesses
count=0
#for calculatiing of minimum number of guessing depends upon range
while count<math.log(upper-lower+1,2):
    count=count+1
    #taking guessing number as input
    guess=int(input("Guess the number: "))

    if x==guess:
        print("Congratulations!💐 you did it in",count,"try")
        #once guessed loop will break
        break
    elif x>guess:
        print("you guessed too small")
    elif x<guess:
        print("You guesses too high")
# if guessing is more than required guesses,shows this output
if count>= math.log(upper-lower+1,2):
    print("\n The number is %d" %x)
    print("\t Better Luck Next Time!😔 ")