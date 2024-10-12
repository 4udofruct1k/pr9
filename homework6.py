list = [33, 48, 52, 33, 19, 52, 100, 60, 73, 88]
print(f"Список: {list}")
min_el = min(list)
max_el = max(list)
if min_el != max_el:
    for i in range(1, len(list)):
        if list[i] == min_el:
            list[i] = max_el
        elif list[i] == max_el:
            list[i] = min_el
print(f"Отредактированный список: {list}")
