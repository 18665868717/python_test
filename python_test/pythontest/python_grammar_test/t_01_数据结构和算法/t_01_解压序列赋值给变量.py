# p=(4,5)
p=[2,3]
x,y=p
print(x,y)


data= [ 'ACME', 50, 91.1, [2012, 12, 21] ]
nama,shares,pirce,date=data
print(nama)
print(shares)
print(pirce)
print(date)

data1= [ 'ACME', 50, 91.1, [2012, 12, 21] ]
nama1,shares1,pirce1,[year,mon,day]=data1
print(nama1)
print(shares1)
print(pirce1)
print(year)

data2 = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_,sha,pir,_,=data2
print(_)

"""问题
如果一个可迭代对象的元素个数超过变量个数时，会抛出一个 ValueError 。 那么怎样才
能从这个可迭代对象中解压出N个元素出来？
"""
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
na, email, *phone_numbers = record
print(na)
print(email)
print(type(phone_numbers),*phone_numbers)