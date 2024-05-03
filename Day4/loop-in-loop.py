i = 1
while i<=3 :
    print("round", i)
    j=1
    while j<=5 :
        print("round i = ", i, "round j = ", j)
        j+=1
    i+=1

for i in range(3) :
    print("round", i)
    for j in range(5) :
        print("round i = ", i, "round j = ", j)