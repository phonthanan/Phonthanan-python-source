  # 1. รับค่า test จากผู้ใช้ 
  # 2. รับค่าอักขระที่ต้องการค้นหาจากผู้ใช้
  # 3. แสดงจำนวนของอักขระในข้อความ text

  # ตัวอย่างหน้า
  # Imsert your text: Phonthanan Ketruskul
  # Character to find: a
  # 2 Letters 'a' found in 'Phonthanan Ketruskul'

print("\n=== ITERATING THROUGH STRING ===")
count = 0
text = input("Insert your text : ")
char = input("Character to find : ")

for letter in text:
    if letter == char:
        count += 1
print(f"{count} letters {char} found in '{text}'")


  # เขียนโปรแกรมตรวจสอบตวามแข็งแรงของ PASSWORD
  # นิยามของ strong password คือ ยาวมากกว่า 8 ตัว, มีอักขระ @ 1 ตัว, มีตัวเลข, มีตัวอักษร
  #
  # ตัวอย่างหน้าจอ
  # Insert your password: Phonthanan
  # Your password is not strong!
  #
  # Insert your password: Test@123
  # Your password is strong

password = input("Insert your password: ")
lenght = len(password)
words = password.split('@')

if len(words) > 1 and password.count('@') == 1:
    left = words[0].isalnum()
    right = words[1].isalnum()
else:
    left = False;
    right = False;

if lenght >= 8 and len(words) == 2 and left == True and right == True:
    print("Your password is strong!")
else:
    print("Your password is not strong")