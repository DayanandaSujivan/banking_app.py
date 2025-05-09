import datetime
from pathlib import Path
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
                print("Invalid Choice! Try Again")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
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
                print("Invalid Choice! Try Again")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
            continue


def admin_choice(choice):
    if choice == 1:
        create_account()
        admin_user()
    if choice == 2:
        print("h")
        admin_user()
    if choice == 3:
        print("h")
        admin_user()
    if choice == 4:
        print("h")
        admin_user()
    if choice == 5:
        print("h")
        admin_user()
    if choice == 6:
        exit()

def user_choice(choice):
    if choice == 1:
        print("h")
        customer_user()
    if choice == 2:
        print("h")
        customer_user()
    if choice == 3:
        print("h")
        customer_user()
    if choice == 4:
        print("h")
        customer_user()
    if choice == 5:
        exit()

def account_data_handle(acc_number,cus_id,acc_type,date_stamp):

    from pathlib import Path

    file_path = Path('Account.txt')
    dict = {}
    if file_path.exists():
        file = open('Account.txt', 'r')
        for line in file:
            values = line.strip().split()
            key = values[0]
            dict[key] = values[1:]
        file.close()

        dict[acc_number] = [cus_id, acc_type, str(date_stamp)] 

        file = open('Account.txt', 'w')
        for key, value in dict.items():
            file.write(f"{key}\t{' '.join(value)}\n")
        file.close()

    else:
        dict[acc_number] = [cus_id, acc_type, str(date_stamp)]
        file = open('Account.txt', 'w')
        for key, value in dict.items():
            file.write(f"{key}\t{' '.join(value)}\n")
        file.close()

def customer_data_handle(cus_id,name,dob,NIC,phone,address):

    from pathlib import Path

    file_path = Path('Customer.txt')
    dict = {}
    if file_path.exists():
        file = open('Customer.txt', 'r')
        for line in file:
            values = line.strip().split()
            key = values[0]
            dict[key] = values[1:]
        file.close()

        dict[cus_id] = [name,dob,NIC,phone,address] 

        file = open('Customer.txt', 'w')
        for key, value in dict.items():
            file.write(f"{key}\t{' '.join(value)}\n")
        file.close()

    else:
        dict[cus_id] = [name,dob,NIC,phone,address] 
        file = open('Customer.txt', 'w')
        for key, value in dict.items():
            file.write(f"{key}\t{' '.join(value)}\n")
        file.close()


def create_account():
    cus_id = create_customer_id()
    name = input("Enter Customer Name[eg:J.Jhon]: ")
    dob = input("Enter Customer DOB[eg:2000-01-30]: ")
    NIC = input("Enter Customer NIC[eg:981640954V]: ")
    phone = input("Enter Customer Phone Number[eg:0766370052]: ")
    address = input("Enter Customer Address[eg:Jaffna]: ")
    acc_number = create_account_number()
    acc_type = input("Enter Account Type[Current, Saving, Fixed]: ")
    date_stamp = datetime.datetime.now()
    account_data_handle(acc_number,cus_id,acc_type,date_stamp)
    customer_data_handle(cus_id,name,dob,NIC,phone,address)
    

def create_account_number():
    file_path = Path('Acc_No.txt')

    if file_path.exists():
        file = open('Acc_No.txt', 'r')
        for line in file:
            num = line.strip()
            lists = num.split("_")
            x = int(lists[1])
            lists[1] = x+1
            num = f"{lists[0]}_{lists[1]}"
        file.close()

        file = open('Acc_No.txt', 'w')
        file.write(f"{num}")
        file.close()
        return num
    else:
        file = open('Acc_No.txt', 'w')
        file.write("A_1")
        file.close()
        return "A_1"
def create_customer_id():
    file_path = Path('Cus_ID.txt')

    if file_path.exists():
        file = open('Cus_ID.txt', 'r')
        for line in file:
            num = line
            lists = num.split("_")
            x = int(lists[1])
            lists[1] = x+1
            num = f"{lists[0]}_{lists[1]}"
        file.close()

        file = open('Cus_ID.txt', 'w')
        file.write(f"{num}")
        file.close()
        return num
    else:
        file = open('Cus_ID.txt', 'w')
        file.write("C_1")
        file.close()
        return "C_1"
        

#***************Main Function****************
user_name = input("Enter user name: ")
password = input("Enter password: ")
user_authorization(user_name,password)