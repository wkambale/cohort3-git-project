from converter import celsius_to_fahrenheit, fahrenheit_to_celsius

print("Temperature Converter")

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice  = input("Choose a conversion (1 or 2): ")

if choice == "1":

    try:
        celsius = float(input("Enter a temperature in Celsius: "))

        fahrenheit = celsius_to_fahrenheit(celsius)

        print(f"{celsius}°C is equal to {fahrenheit}°F")

    except ValueError:
        print("Invalid input. Please enter a number.")

elif choice == "2":
    try:
        fahrenheit = float(input("Enter a temperature in Fahrenheit: "))

        celsius = fahrenheit_to_celsius(fahrenheit)

        print(f"{fahrenheit}°F is equal to {celsius}°C")

    except ValueError:
        print("Invalid input. Please enter a number.")

else:
    print("Invalid choice")