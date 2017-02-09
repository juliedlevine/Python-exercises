# Sum the numbers
# num_list = [12, 5, 7]
# print sum(num_list)

# Largest number
# num_list = [12, 5, 7]
# print max(num_list)

# Smallest number
# num_list = [12, 5, 7]
# print min(num_list)

# Even numbers
# num_list = [12, 5, 2, 6, 55, 3, 45, 32, 66]
# for num in num_list:
#     if num % 2 == 0:
#         print num

# Positive numbers
# num_list = [1, 5, -2, -6, -12, 3, 55]
# for num in num_list:
#     if num > 0:
#         print num

# Positive numbers II
# num_list = [1, 5, -2, -6, -12, 3, 55]
# positive_list = []
# for num in num_list:
#     if num > 0:
#         positive_list.append(num)
# print positive_list

# Multiply a list
# num_list = [1, 5, -2, -6, -12, 3, 55]
# factor = 2
# list = []
# for i in range(len(num_list)):
#     list.append(num_list[i] * factor)
# print list

# Multiply vectors
# list_1 = [2, 4, 5]
# list_2 = [2, 3, 6]
# new_list = []
# for i in range(len(list_1)):
#     new_list.append(list_1[i] * list_2[i])
# print new_list

# Matrix addition
# list_1 = [
#     [1, 3],
#     [2, 4]
# ]
# list_2 = [
#     [5, 2],
#     [1, 0]
# ]
# new_list_1 = []
# new_list_2 = []
# final_list = []
# for i in range(2):
#     new_list_1.append(list_1[0][i] + list_2[0][i])
#     new_list_2.append(list_1[1][i] + list_2[1][i])
# final_list.append(new_list_1)
# final_list.append(new_list_2)
# print final_list

# Matrix addition 2
# list_1 = [
#     [1, 3, 6, 2],
#     [2, 4, 3, 1]
# ]
# list_2 = [
#     [5, 3, 2, 1],
#     [1, 0, 9, 8]
# ]
# new_list_1 = []
# new_list_2 = []
# final_list = []
# for i in range(len(list_1[0])):
#     new_list_1.append(list_1[0][i] + list_2[0][i])
# for j in range(len(list_1[0])):
#     new_list_2.append(list_1[1][j] + list_2[1][j])
#
# final_list.append(new_list_1)
# final_list.append(new_list_2)
# print final_list

# De-dup
# list = ["hello", 5, "julie", 4, 5, "hello", "yes", 3, 5]
# de_dup = []
# for item in list:
#     if item not in de_dup:
#         de_dup.append(item)
# print de_dup

# Matrix multiplication
# list_1 = [
#     [2, -2],
#     [5, 3]
# ]
# list_2 = [
#     [-1, 4],
#     [7, -6]
# ]
# new_list_1 = []
# new_list_2 = []
# final_list = []
#
# new_list_1.append((list_1[0][0]*list_2[0][0]) + (list_1[0][1]*list_2[1][0]))
# new_list_1.append((list_1[0][0]*list_2[0][1]) + (list_1[0][1]*list_2[1][1]))
# new_list_2.append((list_1[1][0]*list_2[0][0]) + (list_1[1][1]*list_2[1][0]))
# new_list_2.append((list_1[1][0]*list_2[0][1]) + (list_1[1][1]*list_2[1][1]))
#
# final_list.append(new_list_1)
# final_list.append(new_list_2)
# print final_list
