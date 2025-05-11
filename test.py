username = "s.ajantha"
password = "CUS_0002_6732"
dict_cus = {}
file = open('Customer.txt','r')
for line in file:
    values = line.strip().split()
    key = values[0]
    dict_cus[key] = values[1:]
    if values[0] = cus_id :
        name = values[1]
file.close()
print(name)
