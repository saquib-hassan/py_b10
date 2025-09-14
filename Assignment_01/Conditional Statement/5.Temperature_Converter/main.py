
""" Write a Python program that takes a temperature 
input in Celsius and converts it to Fahrenheit if the temperature is above 0°C, 
or to Kelvin if the temperature is below 0°C. """

#F=(C×59​)+32 greater thanb zero
#K=C+273.15 less than zero
# exact 0 degree is the freezing point of water

temparature = float(input("Enter the temparature: "))
if temparature > 0:
    f=(temparature*59)+32
    print(f"Temparature is {f:.2f} Fahrenheit")
elif temparature <0:
    k=temparature+273.15
    print(f"Temparature is {k:.2f} Kelvin")
elif temparature == 0:
    f=(temparature*59)+32
    k=temparature+273.15
    print(f"Temparature is {f:.2f} Fahrenheit")
    print(f"Temparature is {k:.2f} Kelvin")