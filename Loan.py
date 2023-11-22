Loanamount = float(input("Enter Loan Amount \n"));
InterestRate = float(input("What is the interest Rate ?\n"));
Tenure = float(input("What is the Loan Tenure? \n"));
MonthlyPayment = float(input("What is the Monthly Payment Amount ? \n"));
Checkmonth = int(input("What is the month to be checked ?\n"));

TotalLoan = Loanamount + ((Loanamount*InterestRate*Tenure)/12/100);
print("Total Loan Amount",TotalLoan)

for i in range(Checkmonth):
    TotalLoan = TotalLoan-MonthlyPayment;
    if TotalLoan < 0:
       print("Full Amount Paid in",(i+1)," months");
       break    
    print("Remaining Loan Amount",TotalLoan," after",(i+1)," payments") 