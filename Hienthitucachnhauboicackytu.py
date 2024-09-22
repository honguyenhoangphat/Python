#Viết chương trình hiển thị các từ theo yêu cầu ra màn hình: “Xin”, “chao!", “Toi", “ten", “la”,
#“{Tên của bạn}”. Các từ cách nhau bởi “--” và {Tên của bạn} được nhập từ bàn phím.

# Input -- PRINT -- Thamso Sep cua PRINT
p1 = input("Nhap ten: ");
print("Toi","ten", "la: ",p1,sep="--")

#Print
#sep: tach rieng cac doi tuong
#end: gia tri cuoi in ra man hinh
#file: ham` print se ghi noi dung vao file
#flush: gia tri mac dinh la False

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)