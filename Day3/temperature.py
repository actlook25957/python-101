temp = input("ป้อนอุณหภูมิ (องศา) :")

degree = int(temp[:-1])
unit = temp[-1].upper()

if unit == "C" :
    print((degree*9/5)+32, "F")
    result = (degree*9/5)+32
    unit_result = "ฟาเรนไฮน์"
if unit == "F" :
    print((degree-32)*5/9 , "C")
    result = (degree-32)*5/9
    unit_result = "องศาเซลเซียส"

print("แปลงตัวเลข = ", temp, "เป็น ", unit_result, " = ", result)
