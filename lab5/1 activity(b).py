def temperature_converter():
    while True:
        print("\nTemperature Converter")
        print("1. Celsius to Fahrenheit and Kelvin")
        print("2. Fahrenheit to Celsius and Kelvin")
        print("3. Kelvin to Celsius and Fahrenheit")
        print("4. Exit")
        choice = input("Enter choice (1/2/3/4): ")

        if choice == '4':
            print("Exiting the converter.")
            break

        try:
            temp = float(input("Enter the temperature: "))
        except ValueError:
            print("Invalid input! Please enter a numeric value.")
            continue

        if choice == '1':
            fahrenheit = (temp * 9/5) + 32
            kelvin = temp + 273.15
            print(f"{temp}°C is equal to {fahrenheit}°F and {kelvin}K.")
        
        elif choice == '2':  
            celsius = (temp - 32) * 5/9
            kelvin = celsius + 273.15
            print(f"{temp}°F is equal to {celsius}°C and {kelvin}K.")
        
        elif choice == '3':  
            celsius = temp - 273.15
            fahrenheit = (celsius * 9/5) + 32
            print(f"{temp}K is equal to {celsius}°C and {fahrenheit}°F.")
        
        else:
            print("Invalid choice! Please select a valid option.")


mal=temperature_converter()
