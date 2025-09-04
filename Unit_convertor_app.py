def inch_to_feet(inch):
    return inch*0.0833333

def feet_to_m(feet):
    return feet * 0.3048

def feet_to_inch(feet):
    return feet/0.0833333

def m_to_feet(m):
    return m/0.3048


print("Welcome to Height Convertor!!")
print("1. Inch to Feet Conversion")
print("2. Feet to Metre Conversion")
print("3. Feet to Inch Conversion")
print("4. Metre to Feet Conversion") 
choice = input("Choose conversion (1-4): ")   

try:
    if choice == "1":
        inch= eval(input("Enter Inches :"))
        print(f"{inch}inch = {inch_to_feet(inch):.2f}feet")
        
    elif choice == "2":
        feet = eval(input("Enter feet :"))
        print(f"{feet}feet = {feet_to_m(feet):.2f}metre")
        
    elif choice == "3":
        feet = eval(input("Enter feet :"))
        print(f"{feet}feet = {feet_to_inch(feet):.2f}inch")
    
    
    elif choice == "4":
        m = eval(input("Enter m :"))
        print(f"{m}metre = {m_to_feet(m):.2f}feet")
        
    else:
        print("INVALID CHOICE")
except ValueError:
    print("Please enter a valid number")


if __name__ == "__main__":
    print("This is a Height Convertor App")        