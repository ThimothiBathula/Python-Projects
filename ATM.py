import time as t

print("Please Insert Card")
#to take time for next line print
t.sleep(5)

#user default password
password=9989

#take user password
YourPass=int(input("Please Enter Your PIN:"))

#Account Balance
balance=10000

#Transactions History for withdrawal and diposite

transactins={"Diposite":[1000],"Withdrawal":[]}

#to iterate the while loop by using n value
n=True  


# this loop for perform operations by using the n value
#if n value false the loop is terminated by defult n value True
while(n):
        
#to check the password if correct or wrong
    if(YourPass==password):
            
        #take time for next line excecution
        t.sleep(6)
        print("--------------------------")
        
        #operations list with options
        print("""Please Select one Option Below\n
           1.Show balance\n
           2.Withdrawal Amount\n
           3.Diposite Amount\n
           4.PIN Change\n
           5.Transaction history\n
           6.Exit""")
        print("--------------------------")
        
        #option for the operations
        option=int(input("Enter Option:"))


        #if user select the option one by press 1 key the show account balance
        if(option==1):
            print("--------------------------")
            print(f"Your Account Balance:{balance}")
            
            #n value true for repeate the loop
            n=True

        #option 2 for the withdrawal Amount from balence
        elif(option==2):
                
            #take user input for withdrawal amount
            WithdrawalAmount=int(input("Enter Amount:"))
            
            #to compare the balance with WithdrawalAmount
            if(balance>=WithdrawalAmount):
                balance-=WithdrawalAmount

                #to add the transaction to transcations
                transactins['Withdrawal'].append(WithdrawalAmount)
                
                print("--------------------------")
                t.sleep(4)
                print("Withdrawal Success")
                n=True
                
            #if WithdrawalAmount is greater than balance then execute this block 
            else:
                t.sleep(4)
                print("--------------------------")
                print("Your Account Has no enough money")
                n=True
                
        #option 3 for deposite the amount into
        elif(option==3):
            t.sleep(4)
            
            #take input for deposite Amount
            deposit=int(input("Enter Amount For Deposite:"))
            print("--------------------------")
            
            #to add the deposite amount to balance
            balance+=deposit
            
            #to add the transaction to transcations
            transactins['Diposite'].append(deposit)
            print("Deposit Success")
            n=True

        #option 3 for pin change
        elif(option==4):
            t.sleep(4)

            # take the otp from user for authentication
            otp=int(input("Enter Otp:"))
            
            #otp must in 4 digits
            if(otp>999 and otp<10000):
                print("--------------------------")
                newPin=int(input("Enter Your New PIN:"))
                rePin=int(input("Enter Again PIN:"))
                if(newPin==rePin):
                    password=newPin
                    t.sleep(4)
                    print("--------------------------")
                    print("Pin change Success")
                    t.sleep(3)
                    print("--------------------------")
                    YourPass=int(input("Please Enter Your New PIN:"))
                    
                else:
                    print("Pin Change not Possible Try Again")
            else:
                    print("Your Otp Not Valid")
            n=True

        #option 5 for the show the transactions
        elif(option==5):
            print("--------------------------")
            print("Diposite")
            print("---------")

            #this for Deposites list
            for i in transactins['Diposite']:
                print(i)
            print("\nWithdrawal")
            print("-----------")

            #this for Withdrawal list
            for i in transactins['Withdrawal']:
                print(i)
            n=True

        #this option for the to Exit  
        elif(option==6):
            t.sleep(2)
            n=False
            
        #if entered any wrong option then execute this block
        else:
            print("Your Entered Wrong Option")
            n=True
            t.sleep(2)
    else:
        t.sleep(6)
        print("Your Entered Wrong Password")
        n=False
    



