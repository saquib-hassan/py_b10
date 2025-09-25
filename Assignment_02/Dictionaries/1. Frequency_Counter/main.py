"""Count the frequency of each element in a list and store the results in a dictionary."""

frequency_list = [1,2,3,4,5,6,1,2,6,45,6]

my_dict = {}
# count = 0

for i in frequency_list:
    if i in my_dict:
        my_dict[i] += 1
        
    else:
        my_dict[i] = 1


print(my_dict)

        
    