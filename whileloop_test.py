

# List of numbers
listOfStuff = [21, 33, 77, 2, 4, 10, 3, 17]

# This while loop starts listing the odd and even from index 7 which is number from 17
count = len(listOfStuff)
print('while loop')
while count > 0:
    count = count - 1
    if listOfStuff[count] % 2 == 0:
        print(f"even - {listOfStuff[count]}")
    else:
        print(f"odd - {listOfStuff[count]}")
    
    
print('-----------------------------------------------------------------')

# this for loop starts listing the odd and even number from index 0 which is 21
print('for loop')
listOfStuff = [21, 33, 77, 2, 4, 10, 3, 17]
for x in listOfStuff:
    if x % 2 == 0:
        print(f"even - {x}")
    else:
        print(f"odd - {x}")


# Task:
# Rewrite the while loop so that it would start listing the odd and even numbers from
# index 0