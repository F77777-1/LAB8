"""
Program Name: Lab8_fatima-2.py
Author: Fatima Abdul
Purpose: Finds area and perimeter of circles and rectangles.
Starter Code: None
Date: 6/20/26
"""

import circle as c
import rectangle as r

# both files have calc_area

choice = 0

while choice != 5:

    print()
    print("Geometry Calculator")
    print("1. Circle Area")
    print("2. Circle Circumference")
    print("3. Rectangle Area")
    print("4. Rectangle Perimeter")
    print("5. Exit")

    choice = int(input("Choice: "))

    if choice == 1:
        radius = float(input("Radius: "))
        area = c.calc_area(radius)
        print("Area =", area)

    elif choice == 2:
        radius = float(input("Radius: "))
        circumference = c.calc_circumference(radius)
        print("Circumference =", circumference)

    elif choice == 3:
        width = float(input("Width: "))
        height = float(input("Height: "))
        area = r.calc_area(width, height)
        print("Area =", area)

    elif choice == 4:
        width = float(input("Width: "))
        height = float(input("Height: "))
        perimeter = r.calc_perimeter(width, height)
        print("Perimeter =", perimeter)

    elif choice == 5:
        print("Bye")

    else:
        print("Invalid choice")

    if choice != 5:
        input("Press Enter...")