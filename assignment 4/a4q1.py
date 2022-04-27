quantity=float(input("number of widgets"))
if quantity>10000:
  price=10
elif quantity>=5000:
 price=20
else:
  price=30
extendedPrice=quantity*price
tax=extendedPrice*.07
total=extendedPrice+tax
print("extended price: ",extendedPrice)
print("tax amount: ",tax)
print("your total: ",total)
