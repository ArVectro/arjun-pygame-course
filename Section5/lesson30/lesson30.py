from random import randint

start = 1

end = 1000

value = randint(start, end)
print("The computer chose a number between ",  start, " and ", end)

guess = None

while guess != value:
    text = input("Guess the number: ")
    guess = int(text)

    if guess < value:
        print("Higher")
    if guess > value:
        print("Lower")

print("Congrats you won!")