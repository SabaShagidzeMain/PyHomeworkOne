hasDriversLicense = input("you have a drivers license - y/n")
isSober = input("you're sober - y/n")
knowsTheWay = input("do you know the way - y/n")

# You're trying to figure out if you should drive home or call a taxi
if (hasDriversLicense == "y" and isSober == "y") and knowsTheWay == "y":
    print("Great! You can drive home!")
elif (hasDriversLicense == "y" and isSober == "y") and knowsTheWay == "n":
    print("Great! Drive home but Use Google Maps!")
elif (hasDriversLicense == "n" or isSober == "n") and knowsTheWay == "y":
    print("Better take a cab")
elif (hasDriversLicense == "y" or isSober == "y") and knowsTheWay == "n":
    print("Better Take a cab and watch the road!")
else:
    print("No drivers license \n Not sober \n And don't know the way \n Should've stayed at home!")
