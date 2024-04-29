age = int(input("age (year):"))

if age >=15 and age <=20:
    print("วัยรุ่น")
elif age >=20 and age <=29:
    print("วัยหนุ่มสาว")
elif age >=30:
    print("วัยผู้ใหญ่")
else :
    print("วัยเด็ก")

if not age >=15:
    print("ไม่ใช่วัยรุ่น")