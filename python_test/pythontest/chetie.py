x=0
y=0
x=y
z=1
m=1
if m=1:
    x=y
    z=1
else:
    z=z + 1
    x=(x*z+y)/z+1
print(x)