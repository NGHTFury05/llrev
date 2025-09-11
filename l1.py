# def prin(n,st):
#     if n<1:
#         return
#     print(st*n)
#     prin(n-1,st)
#     print(st*n)
# prin(7,"Siu")

# def back(n,i=1):
#     if i>n:
#         return
#     back(n,i+1)
#     print(i)
# back(7)
# def parameterized(n,Sum=0):
#     if n<1:
#         print(Sum)
#         return
#     parameterized(n-1,Sum+n)
# parameterized(3)
def functional(n):
    if n<1:
        return 0
    return n+functional(n-1)
print(functional(3))

