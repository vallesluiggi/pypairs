import datetime
num = int(input("Enter the number: "))
timeA = datetime.datetime.now()
array1 = open('array.txt')
array = []
for line in array1:
    line = line.rstrip()
    number = ""
    for x in line:
        if x.find(','):
            number += str(x)
        else:
            array.append(int(number))
            number = ""
def find(array, len, num):
    print("Looking for pair: ", num, " Date: ", timeA.strftime('%m/%d/%Y %H:%S'))
    for i in range(len):
        for j in range(i, len):
            if (array[i] + array[j]) == num:
                print(array[i], array[j])
print("Giving array ", array)
find(array, len(array), num)