# hàm, phương thức, toán tử list khác tương tự với chuỗi

a = ['Hello', 'Vinsofts']
# b = a
# c = list(a)
# d = [i for i in range(10)]

# a += ['Test']

# print(a)

# print(b)

# print(c)

# print(d)

a.append([1,2]) # thêm phần tử

a.extend([1,2]) # thêm theo thứ tự

a.insert([1,2]) # thêm 2 vào vị trí 1

a.pop(1)    #bỏ đi phần tử thứ 1 và tả về giá trị là nó, không truyeenf giá trị mặc định là phần tử cuối cùng

a.remove('Hello')   # loại bỏ phần tử  'Hello' khỏi list, không có sẽ báo lỗi

a.reverse() #đảo ngược list

a.sort()    #săp xếp mặc định tăng dần (bắt buộc phải là số). pram reverse=True để đảo ngược

# a.clear() #xóa hết các phần tử trong mảng

print(a)