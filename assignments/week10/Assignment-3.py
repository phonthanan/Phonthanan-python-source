def deposit():
    balance = 1000.0
    print(f"ยอดเงินเริ่มต้น: {int(balance)} บาท")
    
    try:
        amount_input = input("กรอกจำนวนเงินที่ต้องการฝาก: ")
        amount = float(amount_input)
        
        if amount <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")
            
    except ValueError as e:
        if str(e).startswith("could not convert"):
            print("เกิดข้อผิดพลาด: กรุณากรอกตัวเลขที่ถูกต้อง")
        else:
            print(f"เกิดข้อผิดพลาด: {e}")
            
    else:
        balance += amount
        print("ฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ: {balance:.2f} บาท")
        
    finally:
        print("สิ้นสุดรายการฝากเงิน")