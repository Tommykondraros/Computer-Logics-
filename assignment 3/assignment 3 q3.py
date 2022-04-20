books=int(input("number of books"))
cost=float(input("cost per book"))
total=books*cost
if(total>50):
  shipping=0
else:
  shipping=25
print("total: ")
print(total)
print("shipping charge: ")
print(shipping)
