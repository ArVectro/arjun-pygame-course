#assign number to numA and numB and then subtract numB from numA, and print the result
numberA = float(input("First number: "))
numberB = float(input("Second number: "))
sub = numberA - numberB
print("Result: " + str(sub))
if sub<0:
    print("Negatice number")
else:
    print("Positive Number")