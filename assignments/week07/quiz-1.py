"""
    สร้าง class Rectangle โดยกำหนดให้
    - มี attribute ชื่อ length และ width ที่เก็บข้อมูลความยาวและความกว้างของสี่เหลี่ยม
    - มี method ชื่อ get_area() ที่คืนค่าพื้นที่ของสี่เหลี่ยม
    - มี method ชื่อ get_perimeter() ที่คืนค่ารอบรูปของสี่เหลี่ยม
"""

class Rectangle:
<<<<<<< HEAD
=======

>>>>>>> upstream/main
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to get the area
    def get_area(self):
        return self.length * self.width

    # Method to get the perimeter
    def get_perimeter(self):
<<<<<<< HEAD
        return f"Perimeter = {self.length} + {self.width} = {2 * (self.length + self.width)}"
=======
        return 2 * (self.length + self.width)
>>>>>>> upstream/main

rect = Rectangle(10, 5)
print(rect.get_area())       # Should print 50
print(rect.get_perimeter())  # Should print 30

<<<<<<< HEAD
"""
เขียนคลาส Circle ที่ทำงานคล้ายคลึงกับคลาส Rectangle 
"""

class Circle:
    def __init__(self, radius):
        self.radius = radius

    # Method to get the area
    def get_area(self):
        return 3.14 * self.radius

    # Method to get the perimeter
    def get_perimeter(self):
        return 2 * 3.14 * self.radius


ExCircle = Circle(7)
print(ExCircle.get_area())
print(ExCircle.get_perimeter())
=======


"""
สร้างคลาส Circle ที่ประยุกต์ใช้คลาส Rectangle
ในการคำนวณ พท. และเส้นรอบรูปได้
"""

class Circle:

    # circle ต้องใช้ข้อมูลอะไรบ้าง เพื่อคำนวณ พท. และเส้นรอบรูป
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to get the area สูตรเดิมได้ไหม?
    def get_area(self):
        return self.length * self.width

    # Method to get the perimeter สูตรเดิมได้มั้ย?
    def get_perimeter(self):
        return 2 * (self.length + self.width)
    
myCircle = Circle(....)
print(myCircle.get_area())
print(myCircle.get_perimeter())
>>>>>>> upstream/main
