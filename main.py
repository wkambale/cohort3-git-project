from converter import celsius_to_fahreneheit

print("Temperature Converter")

try:
    celsius = float(input("Enter a temperature in Celsius: "))

    fahrenheit = celsius_to_fahreneheit(celsius)

    print(f"{celsius}°C is equal to {fahrenheit}°F")

except ValueError:
    print("Invalid input. Please enter a number.")