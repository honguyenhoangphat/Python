#SUM_STRING

n = input("Nhap vao day so nguyen: ")
Danhsach_cacso = n.split() # Tach cac so trong chuoi
#print(Danhsach_cacso)

Dayso = map(int,Danhsach_cacso) #ep kieu du lieu cho chuoi
#print(Dayso)

#Tong
Tong = sum(Dayso)
print("Tong day so la: ", Tong)

