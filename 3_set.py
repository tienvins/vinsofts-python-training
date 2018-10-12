# ko chứa các phần tử trùng lặp, không phân biệt sắp xếp, không chứa unhashabale type
a={1,1,2,3,4,5}

a.discard(2)    #loại bỏ khoong có cũng ko sao
a.remove(2) #loại bỏ không có sẽ báo lỗi
a.add(10)

print(a)

print({1,2,3,4,5}-{1,2,3}) #trừ các phần tử

print({1,2,3}-{1,2,3,4,5})  #trừ các phần tử

print({1,2,3}&{2,3,4})    #lấy các phẩn tử chung

print({2,4}|{1,3,5}) #lấy tất cả các phần tử cửa 2 bên

print({2,4}^{1,3,5}) #lấy tất cả các phần tử cửa 2 bên và loại bỏ các phẩn tử trùng nhau
