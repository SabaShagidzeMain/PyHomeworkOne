# Calculate the body mass index of two people
# print out their bmi and compare them
# BMI = kg/m^2
# import math as m

nameOne = input("name of person one")
weightOne = int(input("weight of person one in kgs"))
heightOne = float(input("height of person one in Meters"))
bmiOne = round(weightOne/heightOne**2)

nameTwo = input("name of person two")
weightTwo = int(input("weight of person two in kg"))
heightTwo = float(input("height of person two in meters"))
bmiTwo = round(weightTwo/heightTwo**2)

if bmiOne > bmiTwo:
    print(f"{nameOne}'s bmi ({bmiOne}) is higher than {nameTwo}'s bmi ({bmiTwo})")
elif bmiOne < bmiTwo:
    print(f"{nameTwo}'s bmi ({bmiTwo}) is higher than {nameOne}'s bmi ({bmiOne})")
elif bmiOne == bmiTwo:
    print(f"{nameOne}'s bmi ({bmiOne}) and {nameTwo}'s bmi ({bmiTwo}) are equal")
else:
    print("something went wrong")
