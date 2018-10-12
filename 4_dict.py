a = {'name': 'Vinsofts', 'member': 96}

b = {key: value for key, value in [('name', 'Vinsofts'), ('member',69)]}

a['name']=1 #thay đổi giá trị của key 'name'

a['ten']='None' #thêm 'ten' vs value là None

a.pop('ten','giá trị mặc đink') #xóa key 'tên' và trả về value nếu ko có thì trả về giá trị mặc đinh

a.setdefault('ten') #nếu chưa có key 'ten' thì thêm vào còn neeis có thì trả về value cửa 'ten'

a.update([('a','2'),('b',5)])

print(a)
print(b)
print(b.get('name','giá trị mặc định'))
print(b.keys())
print(b.values())
