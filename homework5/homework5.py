list = [33, 48, 52, 33, 19, 52, 100, 60, 73, 88]
print("элементы списка, которые больше предыдущего элемента: ")
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        print(list[i])
