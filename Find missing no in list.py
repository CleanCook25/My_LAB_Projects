# Python3 program to Find missing
# integers in list


def find_missing(lst):
    max = lst[0]
    for i in lst:
        if i > max:
            max = i

    min = lst[0]
    for i in lst:
        if i < min:
            min = i

    list1 = []

    for num in range(min + 1, max):
        if num not in lst:
            list1.append(num)

    return list1


# Driver code
lst = [1, 2, 4, 6, 7, 9, 10]
print(find_missing(lst))