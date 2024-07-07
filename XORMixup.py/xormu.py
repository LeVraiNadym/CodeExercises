"""
There is an array a with n−1 integers. Let x be the bitwise XOR of all elements of the array. The number x is added to the end of the array a (now it has length n), and then the elements are shuffled.

You are given the newly formed array a. What is x? If there are multiple possible values of x, you can output any of them.

Input

The input consists of multiple test cases. The first line contains an integer t (1≤t≤1000) — the number of test cases. The description of the test cases follows.

The first line of each test case contains an integer n
(2≤n≤100) — the number of integers in the resulting array a.

The second line of each test case contains n integers a1,a2,…,an (0≤ai≤127) — the elements of the newly formed array a.

Additional constraint on the input: 
the array a is made by the process described in the statement; that is, some value of x exists.

Output
For each test case, output a single integer — the value of x, as described in the statement. If there are multiple possible values of x, output any of them.
"""



def solution():
    size_array = int(input())
    current_array = list(map(int, input().split()))
    
    pref = [0] * size_array 
    suff = [0] * size_array
 
    pref[0] = current_array[0]
    for i in range(1, size_array):
        pref[i] = pref[i - 1] ^ current_array[i]
 
    suff[size_array - 1] = current_array[size_array - 1]
    for i in range(size_array - 2, -1, -1):
        suff[i] = suff[i + 1] ^ current_array[i] 

    if i == 0 and suff[i + 1] == current_array[i]:
        print(current_array[i])
        return 
    for i in range(1, size_array-1):
        if pref[i - 1] ^ suff[i + 1] == current_array[i]:
            print(current_array[i])
            return 
 
    print(current_array[size_array-1])
    return 
        
 
size_input = int(input())

while size_input != 0:
    solution()
 
    size_input -= 1

