# เข้าถึงตัวอักษร
name = "Traitawat"
print(name[0:4])
print(name[-2])

# ลบช่องว่าง
name = "  Look  "
print(len(name))
name = name.strip()
print(name)
name = name.lstrip()
print(name)

# แปลงตัวพิมพ์ใหญ่ไปเล็ก และเล็กไปใหญ่
x = "LOOK"
print(x.lower())
y = "look"
print(y.upper())
print(y.capitalize())

# การแทนที่
a = "Traitawat age 23 23"
print(a.replace("23","24"))
print(a.replace("23","24",1))

# การเช็คข้อความ
b = "Traitawat age 23 23"
x =  "23" in b
print(x)

# การต่อกันของข้อความ
fname = "Traitawat"
lname = "Jitchana"
age = "23"
print("Firstname: " + fname + "\tLastname: " + lname + "\tAge: "+ age)

# การจัดรูปการแสดงผล
salary = 500.987622
text = "Firstname: {0}\tLastname: {1}\tAge: {2} \tSalary: {3:.2f}"
print(text.format(fname,lname,age,salary))

# การนับจำนวนคำในประโยค
fruit = "ไปซื้อผลไม้ มีทุเรียน มังคุด แตงโม ทุเรียน"
print(fruit.count("ทุเรียน"))

# การเช็คคำขึ้นต้น
name = "นายลุค"
print(name.startswith("นาย"))
print(name.startswith("นาง"))
print(name.endswith("ลุค"))