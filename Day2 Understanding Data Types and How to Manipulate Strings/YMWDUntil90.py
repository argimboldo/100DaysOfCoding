# Ymwd until 90yo Calculator 
age = input("What's your age (in years)? ")

years_int = int(age)
months_int= years_int*12
weeks_int = years_int*52
days_int  = years_int*365

# Calcs
year_until  = 90-years_int
months_until= (90*12)-months_int
weeks_until = (90*52)-weeks_int
days_until  = (90*365)-days_int

print(f"Your age is {years_int}, that means that you lived {months_int} months, or {weeks_int} weeks, or {days_int} days \n If you'll have luck on your side and will turn 90, you have to live other {year_until} years, or {months_until} months, or {weeks_until} weeks, or {days_until}. Enjoy! :)")
