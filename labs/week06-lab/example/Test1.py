#part2
# Example 1
def greet_person(name):
    """Greets a person by name"""
    print(f"Hello, {name}! Nice to meet you.")

print("Calling greet_person with different names:")
greet_person(5)
greet_person("Bob")
greet_person("Charlie")
print()

# Example 2
def introduce_person(name, age, city):
    """Introduces a person with their details"""
    print(f"Hi! My name is {name}.")
    print(f"I am {age} years old.")
    print(f"I live in {city}.")
    print()

print("Calling introduce_person:")
introduce_person("Diana", 25, "New York")
introduce_person("Eve", 30, "Los Angeles")

#Example 3
def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)

#part3
# Example 1
def add_numbers(a, b):
    """Adds two numbers and returns the result"""
    result = a + b
    return result

print("Using functions that return values:")
sum1 = add_numbers(5, 3)
sum2 = add_numbers(10, 7)
print(f"5 + 3 = {sum1}")
print(f"10 + 7 = {sum2}")
print(f"Sum of both results: {sum1 + sum2}")
print()

#part4
# Example 1
def greet_with_title(name, title="Mr./Ms."):
    """Greets person with optional title"""
    print(f"Hello, {title} {name}!")

print("Using default parameters:")
greet_with_title("Smith")  # Uses default title
greet_with_title("Johnson", "Dr.")  # Custom title
greet_with_title("Brown", "Prof.")  # Custom title
print()

# Example 2
def create_profile(name, age=18, country="Unknown"):
    """Creates a user profile with default values"""
    print(f"Profile: {name}, Age: {age}, Country: {country}")

print("Multiple default parameters:")
create_profile("Alice")  # All defaults
create_profile("Bob", 25)  # Age specified
create_profile("Charlie", 30, "USA")  # All specified
print()

#งานวันนี้
"""
เขียน FUNCTION แปลงหน่วยสกุลเงิน ที่สามารถแปลงเงินจาก
THB <-> USD .. 1 USD = 32 THB

โดยใช้ชื่อและการใช้งาน
function convert_currency(100, "USD")

แสดงผลออกทางจอ
100 THB = 3.3 USD

และทดสอบการใช้งาน function ที่ตัวเองเขียนด้วย

"""
def THB_to_USD(THB):
    """Converts THB to USD"""
    USD = THB / 32
    return USD

def USD_to_THB(USD):
    """Converts USD to THB"""
    THB = USD * 32
    return THB

def convert_currency(Amount, scale):
    """Converts currency between scales"""
    if scale.upper() == "BAHT":
        converted = THB_to_USD(Amount)
        return f"{Amount}THB = {converted:.1f}USD"
    elif scale.upper() == "DOLLAR":
        converted = USD_to_THB(Amount)
        return f"{Amount}USD = {converted:.1f}THB"
    else:
        return "Invalid scale. Use 'Baht' or 'Dollar'"

print("Currency Converter:")
print(convert_currency(100, "Baht"))
print(convert_currency(3.3, "Dollar"))
print()