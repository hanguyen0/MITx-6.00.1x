'''
Test Case 1:
	      balance = 320000
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 29157.09

Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)^12) / 12.0


'''

def payoffdebtbisection(balance, annualInterestRate):
    #payment=29157.09
    originalBalance=balance
    monthlyInterest=annualInterestRate/12
    lowestBalance=0.01

    monthlyPaymentLowerBound=balance/12
    monthlyPaymentUpperBound=(balance*(1+monthlyInterest)**12)/12
    
    while abs(balance)>lowestBalance:    
        balance=originalBalance
        payment=(monthlyPaymentLowerBound+monthlyPaymentUpperBound)/2

        for i in range(1,13):
            monthlyUnpaidBalance=balance-payment
            balance=monthlyUnpaidBalance+monthlyInterest*monthlyUnpaidBalance
            
            print('Month ' + str(i) + ' remaining balance: ' + str(round(balance, 2)))
            print('Final payment ' + str(payment))
        if round(balance)==0:
            break
        elif round(balance)<0:
            monthlyPaymentUpperBound=payment 
        else:
            monthlyPaymentLowerBound=payment
            

    print('Lowest Payment: ' + str(round(payment, 2)))
payoffdebtbisection(320000, 0.2)
