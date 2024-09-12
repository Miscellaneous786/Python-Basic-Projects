def temp_converter():
    temp_scale = input("Enter the scale you want to input \n('c' for Celsius and 'f' for Fahrenheit): ").lower()
    if temp_scale == "c":
        temp_in_c = int(input("Enter the °C temperature: "))
        temp_in_f = (temp_in_c * 1.8) + 32
        print(f"{temp_in_c}°C is equal to {temp_in_f:.2f}°F.")
    elif temp_scale == "f":
        temp_in_f = int(input("Enter the °F temperature: "))
        temp_in_c = (temp_in_f - 32) * 5/9
        print(f"{temp_in_f}°F is equal to {temp_in_c:.2f}°C.")
    else:
        print("Invalid input")
temp_converter()


