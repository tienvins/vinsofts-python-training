import time
import functools

def cong(a=0,b=0):

    print('a + b =',a,'+',b,'=',a+b)

cong()
cong(5)
cong(5,10)
cong(b=5,a=10)

def cong_key(a=0,*,b=0):    # sau dấu * bắt buộc phải truyền cả key và value

    print('a + b =',a,'+',b,'=',a+b)

cong_key(5,b=10)


# def cong_value(a=0,/,b=0):    # trước dấu / bắt buộc chỉ tuyền value (python phiên bảo thấp 2) 

#     print('a + b =',a,'+',b,'=',a+b)

# cong_value(10,b=5)

def ham(a,b,c):   #không dùng key value positional
    print(a)
    print(b)
    print(a+b+c)
ham(3,*[1,2])


def hamreturn(a,b):
    return a,b
A,B=hamreturn(2,3)
print(A,B)

def hamyield():
    yield 'Dòng 1'
    yield 'Dòng 2'
    yield 'Dòng 3'
    yield 'Dòng 4'
    yield 'Dòng 5'
for i in hamyield():
    print(i)
    time.sleep(0.5)

#lambda
hamlambda= lambda a,b,c : a+b+c
print(hamlambda(1,2,3))

#map
k=[[2,5],[9,10]]
print(list(map(hamreturn,*k))) #dùng * trước k giống ví dụ trên theo po

#filter
func= lambda x: x>0
a=[1,-3,5,-2,4,6]
print(list(filter(func,a)))

#
func=lambda x,y:x+y
a=[1,2,3,4,5]
print(functools.reduce(func,a)) # đưa 2 giá trị vào return 1 giá trị và lấy thêm 1 giá trị đưa vào cho đến hết
