  2 h = 20
  3 w = 20
  4 for i in range(h+1):
  5         print(" " * int(w - i) , end="")
  6         print(("* " * i) , end="")
  7         print(" " * int((w) - i) , end="")
  8         print("")