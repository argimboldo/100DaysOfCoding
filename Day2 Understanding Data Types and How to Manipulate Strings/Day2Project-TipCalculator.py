# Day 2 - Tip Calculator 
print  ("Welcome to the Tip Calculator!")

# Input
bill = input("What was the total bill?: $")
perc = input("What percentage tip would you like to give? 10, 12 or 15%? ")
ppl  = input("How many people to split the bill?: ")

# Calc
bill_num = float(bill)
perc_num = int(perc)
ppl_num  = int(ppl)

perc_appl = round((bill_num/100)*perc_num,2)
perc_per_ppl = round(perc_appl/ppl_num,2)

print (f"If you want to give {perc_num}% bill on {bill_num}$, everyone of you have to pay {perc_per_ppl}$")
