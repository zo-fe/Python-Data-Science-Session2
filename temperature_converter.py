def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

temperatures_celsius = [22, 46, 51, 76]

print("Celsius to Fahrenheit conversions:")
for temp in temperatures_celsius:
    fahrenheit = celsius_to_fahrenheit(temp)
    print(f"{temp}°C = {fahrenheit}°F")
