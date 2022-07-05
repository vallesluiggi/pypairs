import datetime
num = int(input("Enter the number: "))
timeA = datetime.datetime.now()
array = [1,9,5,0,20,-4,12,16,7]
def find(array, len, num):
    print("Looking for pair: ", num, " Date: ", timeA.strftime('%m/%d/%Y %H:%S'))
    for i in range(len):
        for j in range(i, len):
            if (array[i] + array[j]) == num:
                print(array[i], array[j])
print("Giving array ", array)
find(array, len(array), num)