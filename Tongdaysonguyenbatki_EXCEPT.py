#SUM_STRING

n = input("Nhap vao day so nguyen: ")
Danhsach_cacso = n.split() # Tach cac so trong chuoi
#print(Danhsach_cacso)
try:

    Dayso = map(float,Danhsach_cacso) #ep kieu du lieu cho chuoi
    Tong = sum(Dayso)
    print("Tong day so la: ", Tong)
except:
    print("Input khong hop le, vui long nhap lai")
