#Programmer: Michael (Mai) Lillie
#Date: 9/12/24
def calculate_total_purchase():
    # Get User Input
    item1 = float(input('Enter first item\'s cost: '))
    item2 = float(input('Enter second item\'s cost: '))
    item3 = float(input('Enter third item\'s cost: '))
    item4 = float(input('Enter fourth item\'s cost: '))
    item5 = float(input('Enter fifth item\'s cost: '))
    # Sum of items, tax, and true total math
    item_sum = item1 + item2 + item3 + item4 + item5
    tax = item_sum * 0.07
    true_sum = tax + item_sum
    #Print the subtotal, tax, and true total
    print(f'Subtotal: {item_sum:.2f} \nTax Amount: {tax:.2f} \nTotal: {true_sum:.2f}')

calculate_total_purchase()
