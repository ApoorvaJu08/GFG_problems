# Given an array arr[] of N non-negative integers representing height of blocks at index i as Ai where the width of each block is 1. Compute how much water can be trapped in between blocks after raining.
# Structure is like below:
# | |
# |_|
# We can trap 2 units of water in the middle gap.



# Input:
# The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows. Each test case contains an integer N denoting the size of the array, followed by N space separated numbers to be stored in array.

# Output:
# Output the total unit of water trapped in between the blocks.

# Constraints:
# 1 <= T <= 100
# 3 <= N <= 107
# 0 <= Ai <= 108

# Example:
# Input:
# 2
# 4
# 7 4 0 9
# 3
# 6 9 9

# Output:
# 10
# 0

# Explanation:
# Testcase 1: Water trapped by block of height 4 is 3 units, block of height 0 is 7 units. So, total unit of water trapped is 10 units.

for _ in range(int(input())):
    size = int(input())
    x = [int(x) for x in input().split()]
    first = x[0]
    result = 0
    for i in range(1, size):
        res = 0
        if i == size - 1:
            res = first - x[size - 1]
        else:
            res = first - x[i]
        if res > 0:
            result += res
    print(result)