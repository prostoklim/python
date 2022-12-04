# a = int(input("a:"))
# b = int(input("b:"))
# lst = []
#
# for aa in range()
#     lst.append(aaa ** 2)
# print(lst)

# x = input("Ввод:")
# print(x[::-1])
# lst = x.split("")
#
# print(lst)

number = input("Число:")
chet = 0
nechet = 0
lst = []

while number != "end":
    number = input("Число:")
    if number.lstrip("-").isdigit():
        # .lstrip("-") - удалить  "-" слева
        number = int(number)
        lst.append(number)
    elif number == "end":
        break #выход из цикла
    else:
        print("Число пж")
        continue #перезапуск

    if number % 2  == 0:
        chet += 1
    else:
        nechet += 1

print(lst)
print(f"Нечетные: {chet}")
print(f"четные")

lst =[-5, -8, 2, 14, 1]
mini = min(lst)
max = max(lst)

lst.[lst.index(mini)]
lst.[lst.index(maxi)]

lst[lst.index(mini)], lst[lst.index(maxi)] = lst[lst.index(maxi)],
print(lst)