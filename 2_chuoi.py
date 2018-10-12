name = 'hello Vinsofts'

print(name)
print()

print('1 ', name.capitalize())

print('2 ', name.upper())

print('3 ', name.lower())

print('4 ', name.title())

print('5 ', name.swapcase())

print('6 ', name[6:None])

print('7 ', name[::-1])

print('8 ', name[-1:5:-1])

print('9  %s %s' % (name[None:5], name[6:None]))    # return của __str__ khi goi string thì nó sẽ lấy return của __str__

print('10 %r %r' % (name[None:5], name[6:None]))    # return của __repr__

print('11 %d' % (1.23456))  # lấy phần nguyên

print('12 %.3f' % (1.23456))    # lấy ra 1 chữ số phần thập phân

print(f'13 {name}')

print('15', name.center(20, '+'))   # ljust, rjust trái phải

print('16', name.join(['1', '2', '3']))

print('17', name.replace('l', '1', 1))  # replace 1 lần

print('18', name.strip('h'))    # căt kí tự 'h' ở hai đâu của chuỗi, lstrip,rstrip trái phải

print('19', name.split('o', 1)) # return về list vs các phần tử đc cắt từ chuỗi nếu gặp 'o' và chỉ cắt 1 lần. có rsplit/lsplit

print('20', name.partition('o'))    # return về tuple gồm 3 phần tử  có rpatititon/lpatititon

print('21', name.count('o', 0, 6))    # đến 'o' có trong name từ 0->6

print('22', name.startswith('l', 2, None))  # return boolean. kiểm tra chuỗi bắt đầu bằng 'l' không (có endswith)

print('22', name.find('l')) # return vị trí đầu tiên xuất hiện của 'l' trong chuỗi (có rfind)

print('22', name.index('l'))    # return vị trí đầu tiên xuất hiện của 'l' trong chuỗi và báo lỗi nếu ko có (có rindex)

print('22', name.islower()) # kiểm tra name có phải chuỗi thường hay ko (tương tự vs các kiểu khác)

print('22', name*5)
