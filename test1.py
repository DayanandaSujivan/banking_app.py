from pathlib import Path

file_path = Path('Customer.txt')
customer_dict = {}

# Assume these variables are already defined somewhere above:
cus_id = "CUS_0000"
name = "Dummy"
dob = "2000-2000-2000"
NIC = "965454444455"
phone = "07555556656"
address = "Navalu"

if file_path.exists():
    file = open('Customer.txt', 'r')
    for line in file:
        values = line.strip().split()
        key = values[0]
        customer_dict[key] = values[1:]
    file.close()
    
    customer_dict[cus_id] = [name, dob, NIC, phone, address]
    

    file = open('Customer.txt', 'w')
    for key, value in customer_dict.items():
        file.write(f"{key}\t{' '.join(value)}\n")
    file.close()

else:
    customer_dict[cus_id] = [name, dob, NIC, phone, address]
    file = open('Customer.txt', 'w')
    for key, value in customer_dict.items():
        file.write(f"{key}\t{' '.join(value)}\n")
    file.close()
