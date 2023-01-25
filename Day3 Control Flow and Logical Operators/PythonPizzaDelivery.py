# Python Pizza Delivery 
print("Welcome to Python Pizza Delivery")
size = input("What size pizza do you want? S, M or L? ")
addpepp = input("Do you want pepperoni? Y o N? ")
extracheese = input("Do you want extra cheese? Y o N? ")

# S pizza: 15$, M pizza: 20$, L pizza: 25$
# Pepperoni: +2$ (for S), +3$  (for M, L)
# Extra cheese: +1$ (any size)
price = 0
if size == "L":
  price += 25
elif size == "M":
  price += 20
elif size == "S":
  price += 15
else:
  print(f"{size} is not a size. Restart the program and choose correct size")
if addpepp == "Y":
  price +=2
if extracheese == "Y":
    price +=1
print (f"You choose a pizza size {size}, {addpepp} pepperoni and {extracheese} extra cheese, so your price is {price}$")
