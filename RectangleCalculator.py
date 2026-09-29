def calculate_area():
    length = int(input("Insert rectangle length: "))
    width = int(input("Insert rectangle width: "))
    area = int(length * width)
    print(f"Area = {area}")

def calculate_perimeter():
    length = int(input("Insert rectangle length: "))
    width = int(input("Insert rectangle width: "))
    perimeter = int(length + width) * 2
    print(f"Perimeter = {perimeter}")

calculation = str(input("Do you want to calculate area or perimeter? "))
if calculation == "area":
    calculate_area()
elif calculation == "perimeter":
    calculate_perimeter()
else:
    print("Invalid response. Please type area or perimeter")

