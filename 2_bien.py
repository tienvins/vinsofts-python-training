# <tên biến> = <giá trị của biến>

# so
s = 123

# list
ds = [i for i in range(6)]  # <=> a=[0,1,2,3,4,5]

# chuỗi
c = 'Tôi là ai.\nTôi là Vinsofts'

# tuple
tp = (1, 2, 3, 4)

# dict
d = {'name': 'Vinsofts'}

print(s, type(s))
print(ds, type(ds))
print(c, type(c))
print(tp, type(tp))
print(d, type(d))



# hashable obiect vs unhashable object
# ds là unhashable tp là hashable

# print(id(ds))
# print(id(tp))

# ds+=[10,11]
# tp+=(10,11)

# print(id(ds))
# print(id(tp))
