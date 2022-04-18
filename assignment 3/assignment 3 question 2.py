item = input("input A or B: ")
quantity = float(input("input any number"))
if(item=="b"):
  unitPrice=20.00
else:
  unitPrice=10.00
extendedPrice=quantity*unitPrice
print("item:")
print(item)
print("Unit Price:")
print(unitPrice)
print("Extended Price:")
print(extendedPrice)
