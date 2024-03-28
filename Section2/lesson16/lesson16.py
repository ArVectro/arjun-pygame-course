techList = ['Apple','Microsoft','SONY','Dell','HP','Samsung']
print(techList[0:2]) # prints first 2 items
techList[0] = 'Tesla' # replaces first item with Tesla
techList.remove('SONY') # removes SONY
print(techList)
techList.insert(3, 'Razer') # puts Razer after third and shifts HP & Samsung to the right
print(techList)
print(len(techList)) # prints the length of the list
print('Microso(ft' in techList) # Checks whether Microsoft is in the list
techList.clear() # Clears the list
print(techList)

fruits = {'banana':0.49, 'orange':1.49, 'apple':1.99} # This is a dictionary
fruits['banana'] = 0.99 # Changes the banana's price to $0.99
print(fruits)
print(fruits['orange']) # prints the price of an orange
fruits['melon'] = 3.01 # makes a new fruit; a melon; and prices it at $3.01
print(fruits)
print('banana' in fruits) # Checks whether banana is in the dictionary of fruits.