# Leap year
y = int(input("Insert the year: "))

# Every year that is evenly divisible by 4
# except every year that is evenly divisible by 100
# unless the year is also evenly divisible by 400

if (y%4)==0:  
  if (y%100)==0: 
    if (y%400)==0: 
      print(f"{y} is leap year!")
    else: 
      print(f"{y} is not a leap year!")
  else:
    print(f"{y} is leap year!")
else:
    print(f"{y} is not a leap year!")
