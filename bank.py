from pathlib import Path
import datetime
import random


def user_authorization(user_name, password):
    dict = {}
    if user_name == 'Admin' and password == 'Admin123':
        admin_user()
    else:
        file_path = Path('Authentication.txt')
        if file_path.exists():
            file = open('Authentication.txt','r')
            for line in file:
                values = line.strip().split()
                key = values[0]
                dict[key] = values[1:]
                if user_name == values[1] and password == values[2] :
                    cus_id = values[0]
            file.close()
            try:
                customer_user(cus_id)
            except UnboundLocalError:
                print("Please Enter Correct User Name Or Password or Register First!")
        else:
            print("Please Enter Correct User Name Or Password or Register First!")

def admin_user():
    while True:
        print("*******************Menu*************************")
        print("1.Create Account: ")
        print("2.Deposit Money")
        print("3.Withdraw Money")
        print("4.Check Balance")
        print("5.Transaction  History")
        print("6.Exit ")
        print("************************************************")

        try:
            choice = int(input("Enter your choice(1-6): "))
            if choice >= 1 and choice <= 6:
                admin_choice(choice)
            else:
                print("Invalid Choice! Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter numeric value")
            continue
        
def customer_user(cus_id):
    dict = {}
    file = open('Customer.txt','r')
    for line in file:
        values = line.strip().split()
        key = values[0]
        dict[key] = values[1:]
        if values[0] == cus_id :
            name = values[1]
    file.close()
    print(f"Welcome! {name}")
    while True:
        print("*******************Menu*************************")
        print("1.Deposit Money")
        print("2.Withdraw Money")
        print("3.Check Balance")
        print("4.Transaction  History")
        print("5.Exit ")
        print("************************************************")

        try:
            choice = int(input("Enter your choice(1-5): "))
            if choice >= 1 and choice <= 5:
                user_choice(choice,cus_id)
            else:
                print("Invalid Choice! Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter numeric value")
            continue


def admin_choice(choice):
    if choice == 1:
        create_account()
        admin_user()
    elif choice == 2:
        print("h")
        admin_user()
    elif choice == 3:
        print("h")
        admin_user()
    elif choice == 4:
        print("h")
        admin_user()
    elif choice == 5:
        print("h")
        admin_user()
    elif choice == 6:
        exit()

def user_choice(choice,cus_id):
    if choice == 1:
        deposite(cus_id)
        customer_user(cus_id)
    elif choice == 2:
        Withdrawal(cus_id)
        customer_user(cus_id)
    elif choice == 3:
        print("h")
        customer_user(cus_id)
    elif choice == 4:
        print("h")
        customer_user(cus_id)
    elif choice == 5:
        exit()

def account_data_handle(acc_number,cus_id,acc_type,date_stamp,NIC):
    nic_exists = False
    file_path = Path('Account.txt')
    dict_acc = {}
    dict_cus = {}
    if file_path.exists(): 
        file = open('Account.txt', 'r')
        for line in file:
            values = line.strip().split()
            key = values[0]
            dict_acc[key] = values[1:]
        file.close()
        file = open('Customer.txt', 'r')
        for line in file:
            values = line.strip().split()
            key = values[0]
            dict_cus[key] = values[1:]
            if values[3] == NIC:
                nic_exists = True
                existing_cus_id = values[0]
                break
        file.close()
        if nic_exists == True:
            dict_acc[acc_number] = [existing_cus_id, acc_type, str(date_stamp)]
            transection(acc_number,existing_cus_id,transferor = "Admin",status = "deposite",amount = "1000",total_amount = "1000",date_stamp = str(date_stamp)) 
        else:
            dict_acc[acc_number] = [cus_id, acc_type, str(date_stamp)] 
            transection(acc_number,cus_id,transferor = "Admin",status = "deposite",amount = "1000",total_amount = "1000",date_stamp = str(date_stamp))            

        file = open('Account.txt', 'w')
        for key, value in dict_acc.items():
            file.write(f"{key}\t{' '.join(value)}\n")
        file.close()

    else:
        dict_acc[acc_number] = [cus_id, acc_type, str(date_stamp)]
        file = open('Account.txt', 'w')
        for key, value in dict_acc.items():
            file.write(f"{key}\t{' '.join(value)}\n")
        file.close()
        transection(acc_number,cus_id,transferor = "Admin",status = "deposite",amount = "1000",total_amount = "1000",date_stamp = str(date_stamp))
        

def customer_data_handle(cus_id,name,dob,NIC,phone,address,user_name,password):
    nic_exists = False
    file_path = Path('Customer.txt')
    dict_cus = {}
    if file_path.exists():
        file = open('Customer.txt', 'r')
        for line in file:
            values = line.strip().split()
            key = values[0]
            dict_cus[key] = values[1:]
            if values[3] == NIC:
                nic_exists = True
        file.close()
        print(nic_exists)
        if nic_exists == False:
            dict_cus[cus_id] = [name,dob,NIC,phone,address]
            user_authentication_credentials(cus_id,user_name,password) 
        file = open('Customer.txt', 'w')
        for key, value in dict_cus.items():
            file.write(f"{key}\t{' '.join(value)}\n")
        file.close()

    else:
        dict_cus[cus_id] = [name,dob,NIC,phone,address] 
        file = open('Customer.txt', 'w')
        for key, value in dict_cus.items():
            file.write(f"{key}\t{' '.join(value)}\n")
        file.close()
        user_authentication_credentials(cus_id,user_name,password)

def user_authentication_credentials(cus_id,user_name,password):
    file = open('Authentication.txt','a')
    file.write(f"{cus_id}\t{user_name}\t{password}\n")
    file.close()


def create_account():
    cus_id = create_customer_id()
    name = input("Enter Customer Name[eg:J.Jhon]: ")
    dob = input("Enter Customer DOB[eg:2000-01-30]: ")
    NIC = input("Enter Customer NIC[eg:981640954V]: ")
    NIC = NIC.strip().lower()
    phone = input("Enter Customer Phone Number[eg:0766370052]: ")
    address = input("Enter Customer Address[eg:Jaffna]: ")
    acc_number = create_account_number()
    acc_type = input("Enter Account Type[Current, Saving, Fixed]: ")
    date_stamp = datetime.datetime.now()
    user_name = name.strip().lower()
    password = create_user_password(cus_id)
    account_data_handle(acc_number,cus_id,acc_type,date_stamp,NIC)
    customer_data_handle(cus_id,name,dob,NIC,phone,address,user_name,password)

def create_user_password(cus_id):

    num = random.randrange(1000,9999)
    password = f"{cus_id}_{num}"
    return password

def create_account_number():
    file_path = Path('Account.txt')

    if file_path.exists():
        file = open('Account.txt', 'r')
        last = []
        for line in file:
            last = line
            acc_no = (last.strip().split()[0])
            code, number = acc_no.split("_")
            new_acc_no = (f"{code}_{(int(number) + 1):04d}")
        file.close()
        return new_acc_no
    else:
        return "ACN_0001"
    
def create_customer_id():
    file_path = Path('Customer.txt')

    if file_path.exists():
        file = open('Customer.txt', 'r')
        last = []
        for line in file:
            last = line
            cus_no = (last.strip().split()[0])
            code, number = cus_no.split("_")
            new_cus_no = (f"{code}_{(int(number) + 1):04d}")
        file.close()
        return new_cus_no
    else:
        return "CUS_0001"
    
def transection(acc_number,cus_id,transferor,status,amount,total_amount,date_stamp):
    dict_trans = {}
    dict_trans[acc_number] = [cus_id,transferor,status,amount,total_amount,date_stamp] 
    file = open('Transection.txt', 'a')
    for key, value in dict_trans.items():
        file.write(f"{key}\t{' '.join(value)}\n")
    file.close()

def deposite(cus_id):
    try:
        acc_no = input("Enter the Account Number to be deposite: ")
        file_path = Path('Account.txt')
        dict_acc = {}
        verify = False
        if file_path.exists(): 
            try:
                file = open('Account.txt', 'r')
                for line in file:
                    values = line.strip().split()
                    key = values[0]
                    dict_acc[key] = values[1:]
                    if values[0] == acc_no and values[1] == cus_id:
                        verify = True
                file.close()
            except Exception as e:
                print("An error occurred while reading Account.txt:", e)

        try:
            deposite_amount = float(input("Enter Deposite Amount: "))
        except ValueError:
            print("Invalid input! Please enter a numeric deposit amount.")
            return

        file_path = Path('Transection.txt')
        dict_depo = {}
        if file_path.exists():
            try:
                file = open('Transection.txt', 'r')
                total_amount = None
                for line in file:
                    values = line.strip().split()
                    key = values[0]
                    dict_depo[key] = values[1:]
                    if values[0] == acc_no:
                        total_amount = values[5]        
                file.close()
                if verify == True:
                    try:
                        total_amount = float(total_amount)
                        total_amount += deposite_amount
                        transection(acc_number = acc_no, cus_id = cus_id, transferor = cus_id, status = "deposite", amount = str(deposite_amount), total_amount = str(total_amount), date_stamp = str(datetime.datetime.now()))
                    except Exception as e:
                        print("An error occurred during transaction:", e)
                else:
                    print("Account verification failed.")
            except IndexError:
                print("Transaction data format is incorrect.")
            except ValueError:
                print("Invalid transaction value. Please check the data.")
            except Exception as e:
                print("An error occurred during deposit:", e)
        else:
            print("Transaction file not found.")
    except Exception as e:
        print("An error occurred:", e)


def Withdrawal(cus_id):
    try:
        acc_no = input("Enter Your Account Number: ")
        dict_withdra = {}
        file = open('Account.txt', 'r')
        access = False
        for line in file:
            values = line.strip().split()
            key = values[0]
            dict_withdra[key] = values[1:]
            if values[0] == acc_no and values[1] == cus_id:
                access = True                
        file.close()
        if access == True:
            try:
                Withdrawal_amount = float(input("Enter Withdrawal Amount: "))
                file_path = Path('Transection.txt')
                dict_withdra = {}
                if file_path.exists():
                    file = open('Transection.txt', 'r')
                    for line in file:
                        values = line.strip().split()
                        key = values[0]
                        dict_withdra[key] = values[1:]
                        if values[0] == acc_no:
                            total_amount = values[5]        
                    file.close()
                    total_amount = float(total_amount)
                    if Withdrawal_amount <= (total_amount - 1000):
                        total_amount -= Withdrawal_amount
                        transection(acc_number = acc_no,cus_id = cus_id,transferor = cus_id, status = "withdrawal",amount = str(Withdrawal_amount),total_amount = str(total_amount),date_stamp = str(datetime.datetime.now()))
                    else:
                        print("Can't Withdraw! Insufficient amount!")
                else:
                    print("You can't withdraw!")
            except ValueError:
                print("Invalid input! Please enter a numeric value.")
            except IndexError:
                print("Transaction data format is incorrect.")
            except Exception as e:
                print("An error occurred during withdrawal:", e)
        else:
            print("Enter Correct Account Number!")
    except FileNotFoundError:
        print("Transaction file not found.")
    except Exception as e:
        print("An error occurred:", e)




        

#***************Main Function****************
user_name = input("Enter user name: ")
password = input("Enter password: ")
user_authorization(user_name,password)