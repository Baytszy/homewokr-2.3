

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count = 0
while count < len(my_list):
    count += 1
    if my_list[count] < 0:
        break
    print(my_list[count])
