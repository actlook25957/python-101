i = 1
while i<=10:
    print("round = ", i)
    if(i == 5):
        break
    i+=1
else: 
    print("end")

i = 1
while i<=10:
    i+=1
    if(i == 5):
        continue
    print("round = ", i)
else: 
    print("end")