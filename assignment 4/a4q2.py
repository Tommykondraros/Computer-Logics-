part=float(input("enter a part number"))
quantity=float(input("enter a quantity"))
if part == 10 or part == 55:
 cost = 1.00
elif part==99:
  cost=2.00
elif part==80 or part==70:
  cost=3.00
else:
  cost=5.00
totalCost=quantity*cost
print("part number: ",part)
print("cost per unit: ",cost)
print("total cost: ",totalCost)
