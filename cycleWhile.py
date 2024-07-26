my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
ind_my_list = 0
# while len(my_list) >= ind_my_list:
#     if my_list[ind_my_list] < 0:
#          print("The end of list, next number negative. Goodbye")
#          break
#     elif my_list[ind_my_list] > 0:
#             print(my_list[ind_my_list])
#             ind_my_list += 1
#     else:
#         ind_my_list += 1
#         continue

# Без применения break и я думаю так будет лаконичнее
while my_list[ind_my_list] >= 0 and len(my_list) >= ind_my_list:
    print(f"The number at index {ind_my_list} => ", my_list[ind_my_list])

    if my_list[ind_my_list] > 0:
        print(f"{my_list[ind_my_list]} is a positive number.\n")
        ind_my_list += 1
    else:
        print("Skipped\n")
        ind_my_list += 1
        continue

print("The end of list, next number negative. Goodbye")

