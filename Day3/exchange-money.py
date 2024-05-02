num = int(input("ป้อนจำนวนเงินที่ต้องการแลก : "))

if num >= 1000:
    print("1000 บาท:", num//1000 , "ใบ")
    num = num%1000

if num >= 500:
    print("500 บาท:", num//500 , "ใบ")
    num = num%500

if num >= 100:
    print("100 บาท:", num//100 , "ใบ")
    num = num%100

if num >= 50:
    print("50 บาท:", num//50 , "ใบ")
    num = num%50

if num >= 20:
    print("20 บาท:", num//20 , "ใบ")
    num = num%20

if num >= 10:
    print("10 บาท:", num//10 , "ใบ")
