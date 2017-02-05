# -*- coding: utf-8 -*-
import math

def getDebt(balance, annualInterestRate, monthlyPaymentRate):
    
    for _ in range(12):
        monthlyInterestRate = annualInterestRate/12.0
        minimumMonthlyPayment = monthlyPaymentRate*balance
        monthlyUnpaidBalance = balance-minimumMonthlyPayment
        balance = math.round(monthlyUnpaidBalance+(monthlyUnpaidBalance+monthlyInterestRate),2)
    
    return balance
