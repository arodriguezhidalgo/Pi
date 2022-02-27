from Algs import BB4
obj = BB4(20000000)
out, error = obj.computePi(8)
print(out)
print(error)

f = open("file.txt", "w")
f.write(str(out))
f.close()