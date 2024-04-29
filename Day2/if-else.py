age = int(input("age (year):"))

if age >=15:
    print("คำนำหน้าเป็นนาย/นางสาว")
else :
    print("คำนำหน้าเป็นเด็กชาย/เด็กหญิง")

if age >=15:
    print("วัยรุ่น")
elif age >=20:
    print("วัยผู้ใหญ่")
elif age >=30:
    print("วัยทำงาน")
else :
    print("วัยเด็ก")