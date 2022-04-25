lastname=input("enter last name: ")
dependents=int(input("enter number of dependents: "))
grossincome=float(input("enter gross income: "))
adjustedGrossIncome=(grossincome)-(dependents*12000)
if adjustedGrossIncome>50000:
  incomeTaxRate=0.20
else:
  incomeTaxRate=0.10
incomeTax=(adjustedGrossIncome*incomeTaxRate)
if incomeTax<0:
 incomeTax=100
print("last name: ",lastname)
print("gross income: ",grossincome)
print("number of dependents: ",dependents)
print("adjusted Gross income: ",adjustedGrossIncome)
print("income tax",incomeTax)