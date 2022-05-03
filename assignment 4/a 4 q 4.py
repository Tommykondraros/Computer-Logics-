quantity=float(input("enter number of tickets: "))
if(quantity>=25):
  pricePerTicket=50
elif(quantity>=10 and quantity<=24):
  pricePerTicket=60
elif(quantity>=5 and     quantity<=9):
  pricePerTicket=70
elif(quantity>5):
  pricePerTicket=75
totalCost=quantity*pricePerTicket
print("number of tickets: ", quantity)
print("price per ticket: ", pricePerTicket)
print("total cost: ", totalCost)