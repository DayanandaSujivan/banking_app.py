from pathlib import Path
import datetime
import random


def user_authorization(user_name, password):
    if user_name == 'Admin' and password == 'Admin123':
        admin_user()
    else:
        customer_user()

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
        
def customer_user():
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
                user_choice(choice)
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

def user_choice(choice):
    if choice == 1:
        print("h")
        customer_user()
    elif choice == 2:
        print("h")
        customer_user()
    elif choice == 3:
        print("h")
        customer_user()
    elif choice == 4:
        print("h")
        customer_user()
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
        else:
            dict_acc[acc_number] = [cus_id, acc_type, str(date_stamp)]             

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
    file = open('Authentication','a')
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
        

#***************Main Function****************
user_name = input("Enter user name: ")
password = input("Enter password: ")
user_authorization(user_name,password)