list = [33, 48, 52, 33, 19, 52, 100, 60, 73, 88]
print(f"Список: {list}")
list.insert(0, list[-1])
list.pop(-1)
print(f"Отредактированный список: {list}")
