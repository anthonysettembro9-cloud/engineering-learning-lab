import random

number = random.randint(1,100)

while True:
    try:
        guess = int(input("Enter a number: "))
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100")
            continue
        break
    except ValueError:
        print("Please enter a valid integer")


count = 1

while (guess != number):
    count += 1
    if (guess > number):
        print("Too high!")
    elif (guess < number):
        print("Too low!")
    while True:
        try:
            guess = int(input("Enter a new number: "))
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100")
                continue
            break
        except ValueError:
            print("Please enter a valid integer")
print("Correct!")
print("Total guesses: ", count)
if (count == 1):
    print("You're a genius!")
elif (count <= 5):
    print("I admire your smartness")
elif (count <= 10):
    print("Not too shabby")
elif (count <= 20):
    print("Lets lock in next time...")
else:
    print("sonion🥀")

