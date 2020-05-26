# Given two rectangles, find if the given two rectangles overlap or not. A rectangle is denoted by providing the x and y co-ordinates of two points: the left top corner and the right bottom corner of the rectangle. Two rectangles sharing a side are considered overlapping.

# Note : It may be assumed that the rectangles are parallel to the coordinate axis.

# rectanglesOverlap

# Input:
# The first integer T denotes the number of testcases. For every test case, there are 2 lines of input. The first line consists of 4 integers: denoting the co-ordinates of the 2 points of the first rectangle. The first integer denotes the x co-ordinate and the second integer denotes the y co-ordinate of the left topmost corner of the first rectangle. The next two integers are the x and y co-ordinates of right bottom corner. Similarly, the second line denotes the cordinates of the two points of the second rectangle in similar fashion.

# Output:
# For each testcase, output (either 1 or 0) denoting whether the 2 rectangles are overlapping. 1 denotes the rectangles overlap whereas 0 denotes the rectangles do not overlap.

# Constraints:
# 1 <= T <= 10
# -104 <= x, y <= 104

# Example:
# Input:
# 2
# 0 10 10 0
# 5 5 15 0
# 0 2 1 1
# -2 -3 0 2

# Output:
# 1
# 0

# Explanation:
# Testcase 1: Given two rectangles overlap each other thus answer returns 1.

def doOverlap(l1_x, l1_y, r1_x, r1_y, l2_x, l2_y, r2_x, r2_y): 
    if (l1_x > r2_x or l2_x > r1_x) :
        return False; 
    if (l1_y < r2_y or l2_y < r1_y):
        return False; 
    return True; 
 
for _ in range(int(input())):
    l1_x, l1_y, r1_x, r1_y = map(int, input().split())
    l2_x, l2_y, r2_x, r2_y = map(int, input().split())
    if doOverlap(l1_x, l1_y, r1_x, r1_y, l2_x, l2_y, r2_x, r2_y):
        print("1")
    else:
        print("0")