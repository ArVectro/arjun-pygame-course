try: # if we do not add the try and except, the input must be an integer - no exceptions
    items = int(input("Type a number of items: "))
    print(items)
    total = 30
    price_per_item = total/items


except ValueError:
    print("That is not an integer.")
except ZeroDivisionError:
    print("You cannot divide by zero.")