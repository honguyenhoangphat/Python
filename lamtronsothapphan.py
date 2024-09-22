#Viết chương trình làm tròn số thập phân A đến B chữ số sau dấu phẩy. A và B được nhập bất kỳ từ bàn phím.
#Hiển thị số A sau khi được làm tròn ra màn hình.
try:

    a = float(input("Nhập số thập phân a: "))
    b = int(input("Số chữ số sau dấu phẩy: "))

    print('Dùng format: {0:.{1}f}'.format(a,b))

    formatedNum = round(a,b)
    print('Dùng round:', formatedNum)

except:
    print("định dạng đầu vào không hợp lệ")