#Programmer: Michael (Mai) Lillie
#Date: 9/12/24
def average_age():
    # Get User Input
    age1 = int(input('Enter first friend\'s age: '))
    age2 = int(input('Enter second friend\'s age: '))
    age3 = int(input('Enter third friend\'s age: '))
    age4 = int(input('Enter fourth friend\'s age: '))
    age5 = int(input('Enter fifth friend\'s age: '))
    # Sum ages
    ageSum = age1 + age2 + age3 + age4 +age5
    # Average the ages
    averageAge = ageSum/5
    # Print the results
    print('Average age is:', averageAge)
# Line which calls the above function.
average_age()
