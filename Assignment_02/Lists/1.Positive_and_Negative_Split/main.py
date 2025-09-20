"""Given a list of integers, separate them into two lists: one with positive numbers and
another with negative numbers."""

# positive_list = [1,2,3,45]
# negative_list = [-1,-3,-4,-6]
# list_of_num = []


positive_list = []
negative_list = []
list_of_num = [1,-1,23,-2,-43,6,8]

for i in range(7):
    if list_of_num[i] > 0:
        positive_list.append(list_of_num[i])
        i =+ i
    else:
        negative_list.append(list_of_num[i])
        i += i

print(positive_list)
print(negative_list)

