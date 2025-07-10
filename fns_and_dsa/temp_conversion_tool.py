# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global conversion factor."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global conversion factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temperature = float(input("Enter the temperature value: "))
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    scale = input("Is this in Celsius or Fahrenheit? (C/F): ").strip().lower()

    if scale == 'c':
        converted = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is equal to {converted:.2f}°F.")
    elif scale == 'f':
        converted = convert_to_celsius(temperature)
        print(f"{temperature}°F is equal to {converted:.2f}°C.")
    else:
        print("Invalid scale. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()
