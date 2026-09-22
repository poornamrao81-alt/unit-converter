print("      unit converter     ")
print("1.convert celcius to kelvin")
print("2.convert kelvin to celcius")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    celcius = float(input("Enter temperature in Celcius: "))
    kelvin = celcius + 273.15
    print("Temperature in Kelvin:", kelvin)
    print("thamks for using this !! hope it helped you !!!")
    
elif choice == "2":
    kelvin = float(input("Enter temperature in Kelvin: "))
    celcius = kelvin - 273.15
    print("Temperature in Celcius:", celcius)
    print("thamks for using this !! hope it helped you !!!")
    
else:
    print("Invalid choice. Please enter 1 or 2.")