#โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย)
# BMI = น้ำหนัก (kg) / ส่วนสูง * ส่วนสูง (m)

w = int(input("weight (kg):"))
h = int(input("high (cm):"))/100
print("BMI", w/(h**2))