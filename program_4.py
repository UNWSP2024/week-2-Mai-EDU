#Programmer Michael (Mai) Lillie
#Date: 9/12/24

def temp_conversion(celsius):
    fahrenheit = 0.0
    fahrenheit = (9/5) * celsius + 32

    return fahrenheit

if __name__ == '__main__':
    celsius = 0.0
    fahrenheit = 0.0
    # Get the Celsius temperature.
    celsius = float(input("Enter a Celsius temperature: "))
    fahrenheit = temp_conversion(celsius)
    # Display the Fahrenheit temperature.
    print ("That is equal to", format(fahrenheit, '.2f'), "degrees Fahrenheit.")
