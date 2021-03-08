mang = []
a = int(input("Nhập số phần tử: \n"))
for i in range(0,a,1):
	x = int(input("Nhập giá trị của mảng "))
	mang.append(x)
	
for t in range(len(mang)):
	if mang[t] < 0:
		mang[t] = 0

print(mang)