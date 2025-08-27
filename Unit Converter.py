'''
PROBLEM STATEMENT:
Create a CLI app that converts units (like km to miles,
Celsius to Fahrenheit, etc.) based on user input.
'''

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print("Unit Converter")
print("1. Kilometers to Miles")
print("2. Miles to Kilometers")
print("3. Celsius to Fahrenheit")
print("4. Fahrenheit to Celsius")

choice = input("Choose an option (1-4): ")

try:
    if choice == '1':
        km = float(input("Enter kilometers: "))
        print(f"{km} km is {km_to_miles(km):.2f} miles")
    elif choice == '2':
        miles = float(input("Enter miles: "))
        print(f"{miles} miles is {miles_to_km(miles):.2f} km")
    elif choice == '3':
        celsius = float(input("Enter Celsius: "))
        print(f"{celsius}°C is {celsius_to_fahrenheit(celsius):.2f}°F")
    elif choice == '4':
        fahrenheit = float(input("Enter Fahrenheit: "))
        print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit):.2f}°C")
    else:
        print("Invalid choice. Please select a valid option.")
except ValueError:
    print("Invalid input. Please enter numeric values.")