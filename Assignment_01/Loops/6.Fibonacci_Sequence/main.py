"""nput N. Print the first N terms of the Fibonacci 
sequence. """

num_of_terms = int(input("How many Fibonacci numbers do you want? "))

first = 0
second = 1

for count in range(num_of_terms):
    print(first)
    next_number = first + second  #calculate the next number
    first = second                #shift the sequence forward
    second = next_number