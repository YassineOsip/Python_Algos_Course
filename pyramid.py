h = 20
w = 20
for i in range(h+1):
	print(" " * int(w - i) , end="")
	print(("* " * i) , end="")
	print(" " * int((w) - i) , end="")
	print("")