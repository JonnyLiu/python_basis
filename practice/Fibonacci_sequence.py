# coding:utf-8

def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b, a+b
        print a,b
    return a

print fib(9)
#
# def fib(n):
#     if n==1 or n==2:
#         return
#     return fib(n-1) + fib(n-2)
# print fib(10)