print("2. Time Converter:")
print("   - Ask user for seconds")
print("   - Convert to hours, minutes, and remaining seconds")
print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print()

# input
seconds = int(input("Enter Seconds"))

# process
hour = seconds // 3600
seconds_remian = seconds % 3600

minute = seconds_remian // 60
seconds_remain = minute * 60

# output
print(f"{seconds} seconds = {hour} hour, {minute} minute, {seconds_remian} second")