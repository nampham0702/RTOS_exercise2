mang = []
a = int(input("Nhập số phần tử: \n"))
for i in range(0,a,1):
	x = int(input("Nhập giá trị của mảng "))
	mang.append(x)

mang.sort()

print("Mảng tăng dần: \n", sorted(mang))