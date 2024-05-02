w = int(input("weight (kg):"))
h = int(input("high (cm):"))/100
bmi =  w/(h**2)

if bmi >=0 and bmi < 18: 
    print("ผอม")
elif bmi >= 18.5 and bmi <=22.9:
    print("สมส่วน")
elif bmi >= 23.0 and bmi <=24.9:
    print("น้ำหนักเกิน")
elif bmi>=25.0 and bmi<=29.9:
    print("โรคอ้วน ระดับที่ 1")
elif bmi>30:
    print("โรคอ้วนระดับอันตราย")    
else : 
    print("กรุณาป้อนค่าให้ถูกต้อง")