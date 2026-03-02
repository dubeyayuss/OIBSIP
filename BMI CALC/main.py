print("Welcome to the BMI Calculator, let's check yout health.")
a=(input("Enter Your name :"))
b=(float(input("Enter Your Weight in kg :")))
c=(float(input("Enter Your Height in m :")))

d=b/(c*c)
print("Your BMI is :",d)

if d<=18.5:
    print("You are underweight and your health risk is Increased (malnutrition).")
elif d>=18.5 and d<=24.9:
    print("You are Healthy Weight and your health is at Lowest risk.")
elif d>=25.0 and d<=29.9:
    print("You are 	Overweight and your health is at Moderate risk.")
elif d>=30.0 and d<=34.9:
    print("You are Obese (Class I) and your health is at High risk.")
elif d>=35 and d<=39.9:
    print("You are Obese (Class II) and your health is at Very High risk.")
elif d<=40:
    print("You are Obese (Class III) and your health is at Extremely High risk.")
else:
    print("Wrong Input.")
