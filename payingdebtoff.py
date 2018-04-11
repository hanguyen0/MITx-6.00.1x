'''
# Test Case 1:
	      balance = 42
	      annualInterestRate = 0.2
	      monthlyPaymentRate = 0.04
	      
	      # Result Your Code Should Generate Below:
	      Remaining balance: 31.38
                    
          # To make sure you are doing calculation correctly, this is the 
          # remaining balance you should be getting at each month for this example
            Month 1 Remaining balance: 40.99
            Month 2 Remaining balance: 40.01
            Month 3 Remaining balance: 39.05
            Month 4 Remaining balance: 38.11
            Month 5 Remaining balance: 37.2
            Month 6 Remaining balance: 36.3
            Month 7 Remaining balance: 35.43
            Month 8 Remaining balance: 34.58
            Month 9 Remaining balance: 33.75
            Month 10 Remaining balance: 32.94
            Month 11 Remaining balance: 32.15
            Month 12 Remaining balance: 31.38
            
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

For each month:
Compute the monthly payment, based on the previous month’s balance.
Update the outstanding balance by removing the payment, then charging interest on the result.
Output the month, the minimum monthly payment and the remaining balance.
Keep track of the total amount of paid over all the past months so far.
Print out the result statement with the total amount paid and the remaining balance.

'''

def payingdebtoff(balance,annualInterestRate,monthlyPaymentRate):
    '''
    balance: the beginning bank balance, can be int or float
    annualInterestRate: float number, the interest rate for a year
    monthlyPaymentRate: float number, the minimum rate to pay off a balance
    This program will pay off a balance within a year and output the leftover balance 
    '''
    #monthlyUnpaidBalance=balance-mininumMonthlyPayment
    #interest=annualInterestRate/12*unpaidBalance
    #newBalance=monthlyUnpaidBalance+interest
    
    for i in range(1,13):
        minimumMonthlyPayment=balance*monthlyPaymentRate
        monthlyUnpaidBalance=balance-minimumMonthlyPayment
        interest=annualInterestRate/12*monthlyUnpaidBalance
        balance=monthlyUnpaidBalance+interest
        #print('Month' + str(i) + ' Remaining balance: ' + str(round(balance,2)))
    print('Remaining balance: ' + str(round(balance,2)))

payingdebtoff(42, 0.2, 0.04)
