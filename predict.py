import joblib
mind = joblib.load("salaryPred.pk1")
inpt = float(input("How Much Experiece do you have .. ?\n\n"))
result = mind.predict([[inpt]])
print("Your estimated Salary will be = ", result[0],end ="/n/n")
