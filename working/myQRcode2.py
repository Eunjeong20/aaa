import qrcode

file_path = r'QRcode\\qrList.txt'

"""
with open(file_path, 'rt', encoding='UTF8') as f :
    read_lines = f.readlines()

    for line in read_lines :
        line = line.strip()
        print(line)
"""

f = open(file_path, 'rt', encoding='UTF8')
read_lines = f.readlines()

for line in read_lines :
    line = line.strip()
    print(line)
    
f.close()