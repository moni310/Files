# i=0
# c=0
# c1=0
# m="shikha"
# while i<len(m):
#     if m[i]=="a" or m[i]=="e" or m[i]=="i" or m[i]=="o" or m[i]=="u":
#         c=c+1
#     else:
#         c1=c1+1
#     i=i+1
# print("vowel=",c)
# print("consonant=",c1)

# def my_fun():
#     global a
#     a=4
# def fun():
#     my_fun()
#     print(a*8)
# fun()

# a=0
# b=1
# while a<=10:
#     print(a)
#     a=b
#     c=a+b
#     b=c

# def fun(*a):
#     print(a*5)
# fun(5,1,4)


def first_function():
    s = 5
    print(s)
    def second_function():
        b=4
        return(s+b)     
    print(second_function())
first_function()