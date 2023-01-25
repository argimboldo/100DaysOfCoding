# BMI Calculator 
w = input("What's your wheight (in kg)? ")
h = input("What's your height (in m)? ")

w_int = int(w)
h_int = float(h)

# Calc BMI
bmi = round(w_int/(h_int**2),2)

if bmi<18.5:
  print(f"Your BMI is {bmi}, so you're underweight (BMI under 18.5)")
if bmi>=18.5 and bmi<25:
  print(f"Your BMI is {bmi}, so you're normal (BMI between 18.5 and 25)")
if bmi>=25 and bmi<30:
  print(f"Your BMI is {bmi}, so you're overweight (BMI between 25 and 30)")
if bmi>=30:
    print(f"Your BMI is {bmi}, so you're obese (BMI over 30)")
