#this will be a program for any math relating to curvature of the earth

#Curvature calculator
Entry_input = input("Test for Expected Curve?: ")
if Entry_input == "yes":
    Secondary_input = input("Inches of curvature or Feet or Miles?: ")
    if Secondary_input == "inches":
        num1 = float(input("Distance in miles: "))
        Expected_curve_inches = 8 * (num1**2)
        print("Expected Curve: " + str(Expected_curve_inches) + " Inches")
    if Secondary_input == "feet":
        num1 = float(input("Distance in miles: "))
        Expected_curve_feet = (8 * (num1**2)) / 12
        print("Expected Curve: " + str(Expected_curve_feet) + " Feet")
    if Secondary_input == "miles":
        num1 = float(input("Distance in miles: "))
        Expected_curve_miles = ((8 * (num1**2)) / 12) / 5280
        print("Expected Curve: " + str(Expected_curve_miles) + " Miles")

#Missing Blockage calculator
if Entry_input == "no":
    Secondary_input = input("Find Missing Blockage based on Expected Curve?: ")
    if Secondary_input == "yes":
        Third_input = input("In Inches, Feet or Miles of Blockage?: ")
        if Third_input == "inches":
            distance = float(input("Distance in miles: "))
            height = input("Height of object in feet: ")
            elevation = input("Elevation in feet: ")
            height = float(height) * 12
            elevation = float(elevation) * 12
            true_height = float(elevation) + float(height)
            Expected_curve_inches = 8 * (distance**2)
            Missing_blockage = (Expected_curve_inches) - float(true_height)
            print("Missing Blockage: " + str(Missing_blockage) + " Inches")
        if Third_input == "feet":
            distance = float(input("Distance in miles: "))
            height = float(input("Height of object in feet: "))
            elevation = input("Elevation in feet: ")
            Expected_curve_feet = (8 * (distance**2)) / 12
            true_height = float(elevation) + float(height)
            Missing_blockage = Expected_curve_feet - float(true_height)
            print("Missing Blockage: " + str(Missing_blockage) + " Feet")
        if Third_input == "miles":
            distance = float(input("Distance in miles: "))
            height = float(input("Height in feet: "))
            elevation = input("Elevation in feet")
            Expected_curve_miles = ((8 * (distance**2)) / 12) / 5280
            true_height = float(elevation) + float(height)
            Missing_blockage = Expected_curve_miles - float(true_height / 5280)
            print("Missing Blockage: " + str(Missing_blockage) + " Miles")