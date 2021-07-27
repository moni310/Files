banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
var=open("list.text","w")
i=0
while i<len(banks_list):
    b=var.write(banks_list[i])
    b=var.write("\n")
    i=i+1
print(b)
var.close()