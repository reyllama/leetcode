
# s = "abcdd"
#
# print(s[3:4])
#
# def is_special(s):
#         if len(set(s))==1:
#             return True
#         elif len(s)%2==1 and len(set(s))==2 and len(set(s[:len(s)//2]+s[len(s)//2+1:]))==1:
#             return True
#         else:
#             return False
#
#     cnt = n
#
#     for i in range(n-1):
#         for j in range(2, n-i+1):
#             if len(set(s[i:i+j]))>2:
#                 continue
#             if is_special(s[i:i+j]):
#                 cnt += 1
#     return cnt

# def lcm(arr):
#     from functools import reduce
#     import math
#
#     prod = reduce(lambda x, y: y*x, arr)
#
#     gcd = arr[0]
#
#     for i in arr[1:]:
#         gcd = math.gcd(gcd, i)
#
#     return prod / gcd**(len(arr)-1)
#
# arr = [2,3,5,6]
# # print(lcm(arr))
# # print(10//1.3)
# #
# # print(5/(5/6)%1==0)
# # print(5//(5/6))
# print(5/(5/6)%1==0)
#
# print(int(7.9 + 1))

# def sol(machines, goal):
#     per_day = sum([1/machine for machine in machines])
#     print(per_day)
#     print(goal/per_day)
#     return round(goal / per_day) if (goal/per_day)%1<1e-8 else int(goal/per_day + 1)
#
#     print(sol([63, 2, 26, 59, 16, 55, 99, 21, 98, 65], 56))
#     print(10//1.5)

print(10//(3/4))
print(10//(1/4))
