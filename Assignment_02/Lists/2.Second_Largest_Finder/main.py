"""Write a program to find the second largest element in a list without using built-in max()
twice or sorting functions."""

my_list = [21,12,4,5,33,20]
second_largest_num = 0
for i in range(6):
    if my_list[0] > my_list[i]:
       
        second_largest_num = my_list[i]
        i = i+1
      
    
print(second_largest_num)
