"""
    Program name: BMI calculation
    @author : Ben Yeamin
"""

print("\n")
print("                         Welcome to BMI Calculation \n                      ********************************\n")
weight = input("Enter your weight in KiloGram: ")

def inch_to_meter (inch):
    meter = inch * 0.025
    return meter

inch = float(input("Enter your hight in inch: "))
print("Your hight in Meter: ", inch_to_meter(inch),"Meter" , "\n")



main_hight = float(inch_to_meter(inch))**2
BMI = float(weight) / float(main_hight)
print("Your BMI value is: ", BMI, "\n")

if BMI < 18.5:
    print("The weight of body weight.Moderate diet will increase the weight")
elif BMI < 24.9:
    print("Good standard of good health.")
elif BMI < 29.9:
    print("Excess weight of body weight.Exercise will reduce excess weight.")
elif BMI < 34.9:
    print("The first layer to be thick.Choices are needed by diet and exercising.")
elif BMI < 39.9:
    print("Second layer to be thick.Moderate diet and needed exercising.")

else:
    print("Extra abundance.The possibility of death swings.Doctors advice is needed.")

print("\n")

input("Enter any key to exit")


