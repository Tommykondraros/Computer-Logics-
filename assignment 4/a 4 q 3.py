principleAmount=float(input("enter principle amount: "))
maturity=float(input("enter maturity amount: "))
if(principleAmount>100000 and maturity==5):
  interestRate=0.6
elif(principleAmount>=50000 and principleAmount<=100000 and maturity== 10):
 interestRate=0.05
elif(principleAmount>=50000 and maturity==5):
 interestRate=0.04
else:
  interestRate=0.02
firstYearInterest=principleAmount*interestRate
print("principle amount: ", principleAmount)
print("interest rate: ", interestRate)
print("interest amount for year: ", firstYearInterest)