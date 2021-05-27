import joblib
mind = joblib.load("salaryPred.pk1")
inpt = float(input("How Much Experiece do you have .. ?"))
result = mind.predict([[inpt]])
print(result)