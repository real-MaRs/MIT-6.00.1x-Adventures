"""using guess and check, get lowest amount of monthly pay to pay off a balance
within a year if interest rate is compounded monthly"""

def getMin(balance, annualInterestRate):
    monthlyInterest = annualInterestRate/12.0
    oldBalance = balance
    minPayment = 10
    months = 0
    while(months < 12):
        monthlyUnpaidBalance = balance - minPayment
        balance = monthlyUnpaidBalance + (monthlyInterest * monthlyUnpaidBalance)
        if(balance <= 0):
            break    
        elif(months == 11 and balance > 0):
            balance = oldBalance
            minPayment = minPayment + 10
            months = -1
            
        months = months + 1    
        
    print(minPayment)