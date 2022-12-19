users={}
name={}
status=""

def displaymenu():
    status=input("Are you a Registered Customer? Y/N? Press Q to quit: ")
    if status=="Y":
        oldUser()
    elif status=="N":
        newUser()
    elif status=="Q":
        print("\nExit Successfully\n")

def newUser():
    yourname=input("Enter your full name: ")
    createLogin=input("Create your username: ")
    if createLogin in users:
        print("\nUsername already exists!\n")
    else:
        createPass=input("Create Password: ")
        DOB=input("Enter your DOB in DD/MM/YYYY format: ")
        Aadhar=int(input("Enter your unique Aadhar number: "))
        users[createLogin]=createPass
        name[yourname]=DOB
        print("\nUser Created\n")

def oldUser():
    login=input("Enter Username: ")
    passw=input("Enter Password: ")

    if login in users and users[login]==passw:
        print("\nLogin Successful!\n")
        print(f"Hi {login}!")
        print("What do you want to do today?\n1.Check Balance\n2.Withdraw Money\n3.Deposit Money\n4.Transfer Money\n5.GST Calculator\n6.Logout")
        balance=1000
        while True:
            a=int(input("Enter your choice: "))
            if a==1:
                print(f"Your Current Balance is {balance}")
            elif a==2:
                withdraw=float(input("Enter amount to withdraw: "))
                if withdraw>0 and withdraw<=balance:
                    balance-=withdraw
                    print("Remaining Balance:",balance)
                elif withdraw>balance:
                    print("Insufficient Funds in your account")
                else:
                    print("None withdrawl made!")
            elif a==3:
                deposit=float(input("Enter the amount too add: "))
                if deposit>0:
                    balance+=deposit
                    print("New Balance:",balance)
                else:
                    print("None Deposit made!")
            elif a==5:
                if balance<=250000 :
                    print("No GST for your current balance")
                elif balance>250000 and balance<=500000:
                    print("Your GST found is:","%.2f"%(balance*0.05))
                elif balance>500000 and balance<=750000:
                    print("Your GST found is:","%.2f"%((balance*0.10)+12500))
                elif balance>750000 and balance<=1000000:
                    print("Your GST found is:","%.2f"%((balance*0.15)+37500))
                elif balance>1000000 and balance<=1250000:
                    print("Your GST found is:","%.2f"%((balance*0.20)+75000))
                elif balance>1250000 and balance<=1500000:
                    print("Your GST found is:","%.2f"%((balance*0.25)+125000))
                elif balance>1500000:
                    print("Your GST found is:","%.2f"%((balance*0.30)+187500))
            elif a==6:
                print("Logout Successfull!")
                break        
    else:
        print("\nInvalid username or password\n")

while status!="q":
    displaymenu()


    


    


