start, stop = 1,5
sum = 0

while (start<=stop) :
    num = int(input("ป้อนตัวเลข = "))
    sum+=num
    start+=1

avg = sum/stop
print("sum = ", sum)
print("avg = ", avg)