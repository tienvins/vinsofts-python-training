# f= open('tenfile.txt')
# data=f.read()
# f.close()
# print(data)

with open('tenfile.txt') as f:
    data= f.read()
print(data)

# f=open('tenfile.txt','a+')
# f.write('Dòng n')
# f.close()