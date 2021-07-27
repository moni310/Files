var=open("people.txt","a")
var.write(" i am closing shop")
var=open("people.txt","r")
print(var.read())
var.close