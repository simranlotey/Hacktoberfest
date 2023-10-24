import string
import time

out = "hello world"

letters = string.printable

cur = ""

for i in out:
    for j in letters:
        time.sleep(0.05)
        print(cur,j,sep="")
        if i == j:
            cur += j
            break
