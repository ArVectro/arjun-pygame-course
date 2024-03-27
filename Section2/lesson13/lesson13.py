# speed limit = 100 mph, speed minimum = 20 mph, how do we check?
carSpeed = int(input("What is your speed right now? "))
if carSpeed > 100:
    print('You drive too fast!')
elif carSpeed < 20:
    print('You drive too slow!')
else:
    print('Your speed is perfect!')
print('Ready')