'''
 Test Case 1:
	      balance = 3329
	      annualInterestRate = 0.2

	      Result Your Code Should Generate:
	      -------------------
	      Lowest Payment: 310

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

The following variables contain values as described below:
    balance - the outstanding balance on the credit card
    annualInterestRate - annual interest rate as a decimal

Now imagine that we try our initial balance with a monthly payment of $10.
If there is a balance remaining at the end of the year,
how could we write code that would reset the balance to the initial balance,
increase the payment by $10, and try again (using the same code!) to compute the balance at the end of the year,
to see if this new payment value is large enough.
'''

def pay_debt_off_in_a_year(balance, annualInterestRate):
    payment=10
    originalBalance=balance
    while balance>0:
        for i in range(1,13):
            monthlyInterest=annualInterestRate/12
            monthlyUnpaidBalance=balance-payment
            balance=monthlyUnpaidBalance+monthlyInterest*monthlyUnpaidBalance
            print('Month ' + str(i) + ' remaining balance: ' + str(round(balance)))
            print('Final payment ' + str(payment))
        if balance<=0:
            break
        else:
            balance=originalBalance
            payment+=10
        
    print('Lowest Payment: ' + str(round(payment)))
    
#THis program runs for 38 seconds   

pay_debt_off_in_a_year(3329, 0.2)

