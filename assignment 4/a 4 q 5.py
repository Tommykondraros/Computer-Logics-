salary=float(input("salary amount"))
lastName=input("enter last name")
jobLevel=float(input("enter job level"))
if(jobLevel>=10):
 bonusRate=0.25
elif(jobLevel>=5):
 bonusRate=0.2
else:
 bonusRate=0.1
bonus=salary*bonusRate
print("last name: ", lastName)
print("bonus: ", bonus)