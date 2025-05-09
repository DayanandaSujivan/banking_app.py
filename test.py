import datetime
from pathlib import Path

file_path = Path('Account.txt')

if file_path.exists():
            file = open('Account.txt', 'r')
            last = []
            for line in file:
                last = line
            acc_no = (last.strip().split()[0])
            code, number = acc_no.split("_")
            new_acc_no = (f"{(int(number) + 1):04d}")
            print(f"{code}_{new_acc_no}")
else:
        file = open('Account.txt', 'w')
        file.write("ACN_0001")
        file.close()