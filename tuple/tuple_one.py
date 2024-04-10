# tuples are immutable

coordinates = (4,5)
print(coordinates)
print(coordinates[0])
print(coordinates[1])

mixData = (0,"Zero",1,"One")
print(mixData)
print(mixData[0])
print(mixData[1])
print(mixData[2])
print(mixData[3])

tupleOfList = ([1,2,3],[4,5,6])
print(tupleOfList[0])
tupleOfList[0][0] = 8
print(tupleOfList[0])