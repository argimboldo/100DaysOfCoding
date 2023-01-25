# Love Calculator
print("Welcome to Love Calculator!")
name1 = input ("insert your name here: ")
name2 = input ("insert you boyfriend/girlfiend name here: ")

# T      L
# R      O
# U      V
# E      E

combinednames = name1 + name2
lower_combinednames = combinednames.lower()

t = lower_combinednames.count("t")
r = lower_combinednames.count("r")
u = lower_combinednames.count("u")
e = lower_combinednames.count("e")

l = lower_combinednames.count("l")
o = lower_combinednames.count("o")
v = lower_combinednames.count("v")

true = t+r+u+e
love = l+o+v+e
truelove = (true+love)


# less than 10 or greater than 90: "Your score is x, you go togheter like cocke and mentos"
# between 40 an 50: "your score is y, you are alright togheter"
# Oterwhise: "Your score is z"

if truelove <10 or truelove>90:
  print (f"Your score is {truelove}, you go togheter like cocke and mentos!")
elif truelove >=40 and truelove<=50:
  print (f"your score is {truelove}, you are alright togheter!")
else:
  print (f"your score is {truelove}")
