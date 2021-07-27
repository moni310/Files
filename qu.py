f=open("question3.text","r")
a=open("delhi.text","w")
b=open("shimla.text","w")
c=open("other.text","w")
d=f.read()
e=d.split("\n")
print(e)
i=0
while i<len(e):
    if "delhi" in e[i]:
        a.write(e[i])
        a.write("\n")
    elif  "shimla" in e[i] :
        b.write(e[i])
        b.write("\n")
    else:
        c.write(e[i])
        c.write("\n")
    i=i+1
a=open("delhi.text","r")
print(a.read())
b=open("shimla.text","r")
print(b.read())
c=open("other.text","r")
print(c.read())
f.close()
a.close()
b.close()
c.close()
    

