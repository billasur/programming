#how many seconds
a= input("how many years?")
a= int(a)*31536000
b= input("how many months?")
b= int(b)*2592000
c= input("how many weeks?")
c= int(c)*604800
d= input("how many days?") 
d= int(d)*86400
e= input("how many hours?")
e= int(e)*3600
f= input("how many minutes?")
f= int(f)*60
g= input("how many seconds?")
h= int(a)+ int(b) +int(c) + int(d) + int(e) + int(f) + int(g)
print("total seconds are" , int(h))
