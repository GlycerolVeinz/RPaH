#převod Celsia na Fahrenheita tF=1.8⋅tC+32

def celsius_to_stupid():

    while True:

        celsius_temperature = input("Type in temperature in Celsius:")
        
        if celsius_temperature.isdecimal() == False:
            print("ERROR, not a number")
        
        else:
            fahrenheit_temperature = (float(celsius_temperature) * 1.8) + 32
            print("Temp in fahrenheit is: ", fahrenheit_temperature)
            break

celsius_to_stupid()
