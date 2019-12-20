balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
	      
t=0
for i in range (12):
    print "Month:",
    print i+1
    p = monthlyPaymentRate * balance
    print "Minimum monthly payment:",
    print ("%.2f" % p)
    balance = (balance - p)*(1 + annualInterestRate/12)
    print "Remaining balance:",
    print ("%.2f" % balance)
    t +=p
print "Total paid:",
print ("%.2f" % t)
print "Remaining balance: ",
print ("%.2f" % balance)    