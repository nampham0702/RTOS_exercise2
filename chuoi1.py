c = input("Nhập chuỗi: ")
words =[word for word in c.split(" ")]
print (" ".join(sorted(list(set(words)))))