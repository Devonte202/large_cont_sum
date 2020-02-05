"""
Problem: Given an array of integers find the largest continuous sum
input: list (positive & negative integers)
output: number(integers)

Examples: 
large_cont_sum([1,2,-1,3,4,10,10,-10,-1]) == 29
large_cont_sum([1,2,-1,3,4,-1]) == 9
large_cont_sum([-1,1]) == 1
large_cont_sum([0,0,0,-1,1]) == 1
large_cont_sum([-1,-2,-1,-3,4,10,10,-10,-1]) == 17
large_cont_sum([-1,1,-1,-2,-1,-3,4,10,10,-10,-1]) == 17
large_cont_sum([]) == None

Data Structure: Dictionary 
Algorithm: 
0: Create a biggest_num_now variable initialized with 0
1: Create a num_sum variable initialized with 0
2: Loop through list
    I: add each number to the num_sum variable
    II: if num_sum is greater than biggest_num_now, reassign biggest_num_now to num_sum
3: If the list only has two numbers in it with a sum of 0, biggest_num_now = the largest number in the list
4: Return the biggest_num_now variable
"""

def large_cont_sum(num_list):
    num_list = [num for num in num_list if num != 0]
    biggest_num_now = 0
    num_sum = 0
    if len(num_list) == 0:
        return None
    if len(num_list) <= 2:
        return max(num_list)
    for num in num_list:
        num_sum += num 
        if num_sum > biggest_num_now:
            biggest_num_now = num_sum
    return biggest_num_now

print(large_cont_sum([1,2,-1,3,4,10,10,-10,-1]) == 29)
print(large_cont_sum([1,2,-1,3,4,-1]) == 9)
print(large_cont_sum([-1,1]) == 1)
print(large_cont_sum([0,0,0,-1,1]) == 1)
print(large_cont_sum([-1,-2,-1,-3,4,10,10,-10,-1]) == 17)
print(large_cont_sum([-1,1,-1,-2,-1,-3,4,10,10,-10,-1]) == 17)
print(large_cont_sum([2]) == 2)
print(large_cont_sum([]) == None)
