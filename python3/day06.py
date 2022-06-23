# First try
# Enter your code here. Read input from STDIN. Print output to STDOUT
# T = int(input())
# 
# for j in range (0,T):
#     S = input()
# 
#     for i in range(0,len(S)):
#         if i % 2 == 0:
#             print(S[i], end="")
#     print(" ", end="")    
#     
#     for i in range(0,len(S)):
#         if i % 2 != 0:
#             print(S[i], end="")
#     print(" ", end="")


# Enter your code here. Read input from STDIN. Print output to STDOUT
# read the input
N = int(input())
for i in range(0, N):
    string = input()

    for j in range(0, len(string)):
        if j % 2 == 0:
            print(string[j], end="")
    print(" ", end="")

    for j in range(0, len(string)):
        if j % 2 != 0:
            print(string[j], end="")

    print("")

