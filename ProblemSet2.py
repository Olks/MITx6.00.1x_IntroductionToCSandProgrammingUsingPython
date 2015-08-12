## ex 1
balance=4213
annualInterestRate=0.2
monthlyPaymentRate=0.04

minmp=1
reb=balance
totalpaid=0
for i in range(12):
    minmp=reb*monthlyPaymentRate
    reb=reb-minmp+(annualInterestRate/12)*(reb-minmp)
    totalpaid+=minmp    
    print("Month: "+str(i+1))
    print("Minimum monthly payment: "+str(round(minmp,2))) 
    print("Remaining balance: "+str(round(reb,2)))
    
print("Total paid: "+str(round(totalpaid,2)))
print("Remaining balance: "+str(round(reb,2)))



## ex 2
balance=3926
annualInterestRate=0.2

r=annualInterestRate
# p - min mothly payment
q=1+r/12.0
p=(balance*(r/12.0)*q**11)/(q**12-1)
if p%10>0: p=p-p%10+10
print("Lowest Payment: "+str(int(p)))

def calculate(K, r, n):
    q = 1.0 + annualInterestRate/12
    return (K*(q**n)*((q - 1))/(q**n - 1))

r=annualInterestRate
lower_bound=balance/12
upper_bound=(balance*(1+r)**12)/12.0
# p - min mothly payment
q=1+(r/12.0)
p=(balance*(r/12.0)*q**11)/(q**12-1)
print("Lowest Payment: "+str(round(p,2)))

