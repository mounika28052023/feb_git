# Simple bank atm
# this is atm program using control statements
a='''
1.deposit
2.withdraw
3.balance enquiry
4.exit
'''
name="mounika"
password="12345"
print("welcome to python life atm")
user_name=input("enter your name:")
pass_word=input("enter your password:")
balance =10000
if name==user_name and password==pass_word:

 while True:
    print(a)
    option=int(input("enter your option:"))
    if option==1:
     credit_amount=int(input("enter your amount:"))
     if credit_amount<=0:
          print("please enter the positive amount:")
     else:
          balance+=credit_amount
          print("deposit sucucessfully, your new balance is:",balance)
    elif option==2:
        debit_amount=int(input("enter the amount:"))
        if debit_amount<=balance:
            balance-=debit_amount
            print("withdrawl sucuessfully,your new balance is:",balance)
        else:
         print("insufficient funds")   
    elif option==3:
        print("your current balance is:",balance) 
    elif option==4:
       print("you are exit") 
       break         
    else:
     print("invalid option")    
else:
   print("invalid transaction details")    








