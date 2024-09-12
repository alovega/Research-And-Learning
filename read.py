
import csv

with open('read.txt', 'r') as f:
    print('\n\n')
    print(f.readline())
    print('\n\n')

    print(f.read())


print('\n\n')

print("Filename is '{}'.".format(f.name))

if f.closed:
    print("File is closed.")

else:
    print("File isn't closed")


print('\n')
with open('read.txt') as f:
    line = f.readline()

    while line:
        print(line, end='')
        line=f.readline()

print('\n\n')


with open('read.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line)

print('\n\n')

with open('dataquest_logo.png', 'rb') as rf:
    with open('dataquest_copy_logo.png', 'wb') as wf:
        for b in rf:
            wf.write(b)

print('\n\n')

with open('chocolate.csv') as f:
    reader = csv.reader(f, delimiter=',')

    for row in reader:
        print(row)

print('\n\n')

with open('chocolate.csv') as f:
    reader = csv.DictReader(f, delimiter=',')

    for row in reader:
        print(row)