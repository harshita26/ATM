import getpass

# creatinga lists of users, their PINs and bank statements
user_list=['user1','user2','user3','user4']
pin_list=['1111','2222','3333','4444']
money=[1000,2000,3000,4000]
tries=0

print("\n\n WELCOME TO A BANK ATM \n\n")

def withdraw_money(withdr,money1):
    if(withdr< money1[n]):
        withdraw_bal=money1[n]-withdr
        money1[n]=withdraw_bal
        print('*'*15)
        print("YOUR NEW BALANCE IS: ",money1[n])
      
    else:
        print("INSUFFICIENT BALANCE")        
#define pin verification
def verifypin(pin1,pin2,j):
    if pin2==pin1[j]:
        return True
    else:
        return False    

# while loop checks existance of the enterd username
while True:
    name=input("ENTER USER NAME: ")
    name=name.lower()
    if(name ==user_list[0]):
        n=0
        break
    elif(name==user_list[1]):
        n=1
        break
    elif(name==user_list[2]):
        n=2
        break
    elif(name==user_list[3]):
        n=3
        break
    else:
        print(""" **********************************
------- INVALID USER NAME ---------
*********************************** \n""")
# comparing pin   
while tries<3:
    pin=str(getpass.getpass('PLEASE ENTER PIN: '))
    if verifypin(pin_list,pin,n):
        print(""" **********************************
----------PIN ACCEPTED-----------
***********************************\n""")
        print("LOGIN SUCCESSFUL, LET'S CONTINUE")
        print(f"""***********************************
{user_list[n]} WELCOME TO ATM
**************************
--------ATM SYSTEM-------
-------------------------
*************************\n""")
        break
    else:
        tries+=1
        print(""" **********************************
------- INVALID USER PIN -------
********************************** \n""")
if tries==3:
    print("""-----------------------------------
***********************************
3 UNSUCCESFUL PIN ATTEMPTS, EXITING
!!!!!YOUR CARD HAS BEEN LOCKED!!!!!
***********************************
----------------------------------- \n""")
    exit()
           
# in case of a valid pin- continuing, or exiting       
while True:
    print("""SELECT FROM FOLLOWING OPTIONS: 
STATEMENT  (S) 
WITHDRAW   (W) 
ADD MONEY  (A)  
CHANGE PIN (P)  
QUIT       (Q) \n""")
    option_value=input("YOUR OPTION: ")
    if (option_value=='s' or option_value=='S'):
        print(f"""--------------------------
**************************
{user_list[n]} YOU HAVE {money[n]} RUPEE ON YOUR ACCOUNT.
**************************
 ------------------------- \n""")
        
    elif (option_value=='w' or option_value=='W'):
        print('*'*15)
        try:
            withdraw=int(input("ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW: "))
            withdraw_money(withdraw,money)
        
        except:
            print("ENTER ONLY A DIGIT\n")
        else:
            print("\n")

    elif(option_value=='A' or option_value=='a'):
        print('*'*15)
        try:
            add=int(input("ENTER AMOUNT YOU WANT TO ADD: "))
            add_bal=money[n]+add
            print("YOUR NEW BALANCE IS: ",add_bal)
            money[n]=add_bal
            
        except:
            print("ENTER ONLY A DIGIT\n")
            
        else:
            print("\n")
        
    elif(option_value=='p' or option_value=='p'):
        print("*"*15)
        new_pin=str(getpass.getpass('PLEASE ENTER PIN: '))
        if(new_pin != pin_list[n] and len(new_pin)==4 and new_pin.isdigit()):
            conform_pin=str(getpass.getpass("CONFIRM NEW PIN: "))
            if(new_pin==conform_pin):
                pin_list[n]=new_pin
                print(f"YOUR NEW PIN IS UPDATED \n")
    
            else:
                print("PIN MISMATCH \n")
        else:
            print("AND MUST BE DIFFERENT TO PREVIOUS PIN AND UNIQUE INTEGER VALUE \n")                 
        
    elif(option_value=='Q' or option_value=='q'):
        print("*"*15)
        exit("THANKS TO VISIT  \n")
        
        
    else:
        print("*"*15)
        print("RESPONSE NOT VALID \n")
    
       










        
