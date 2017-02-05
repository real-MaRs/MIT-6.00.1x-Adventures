""" Using bisection search, find the lowest amount of money you would need to pay a month to 
pay off a balance within a year if the interest rate is compounded monthly"""
def getMinPayment(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate/12.0
    lower = balance/12.0
    upper = (balance*(1 + monthlyInterestRate)**12)/12.0
    month = 0
    oldBalance = balance
    
    while(month < 12):
        minPayment = (lower+upper)/2
        monthlyUnpaidBalance = balance - minPayment
        balance = monthlyUnpaidBalance + (monthlyUnpaidBalance * monthlyInterestRate)
        if(month == 11 and balance < -1):
            month = -1
            upper = minPayment
            balance = oldBalance
        elif(month == 11 and balance > 0):
            month = -1
            lower = minPayment
            balance = oldBalance
        month = month + 1
        
    print(round(minPayment, 2))