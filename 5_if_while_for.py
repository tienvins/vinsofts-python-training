a=2

#if
if(a==1):
    print('a=1')
elif(a==2):
    print('a=2')
elif(a==3):
    print('a=3')
else:
    print('a>3')

#while
print()
print('while')
i=0
while(i<5):
    print(i)
    i+=1

#for mảng
print()
b=[1,2,'ass',7,'bdd']
print('for')
for i in b:
    print(i)

#for chuỗi
print()
c='abcdef'
print('for chuỗi')
for i in c:
    print(i)

#for sử dụng range
print()
print('for range')
for i in range(1000,1005):
    print(i)

print()


#try
try:
    123+'abc'
except:
    print('Lỗi')

