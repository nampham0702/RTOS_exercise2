c = input("Nhập chuỗi: ")
d = 0
s = 0
name = [word for word in c. split(" ")]
for words in range(len(name)):
	if name[words][0] != name[words][0].upper():
		s = s + 1
	else:
		d = d + 1
print(d," đúng, ",s," sai.")