file=open("count.text","r")
c=0
b=file.read()
colist=b.split("\n")
i=0
while i<len(colist):
    if i:
        c=c+1
    i=i+1
print(c)
file.close()