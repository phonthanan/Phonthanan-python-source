"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""

def get_temperatures():

    temps = [30, 32, 33, 28, 29, 34, 27]
    return temps

def analyze_temps(temp_list):

    average = sum(temp_list) / 7
    highest = max(temp_list)
    lowest = min(temp_list)
    return (average, highest, lowest)

def display_analysis(average, highest, lowest):
    print("Temperature Analysis for this Week:")
    print("Average: %.1f C" % average)
    print("Highest: %.1f C" % highest)
    print("Lowest: %.1f C" % lowest)

temps = get_temperatures()
print(temps)
result = analyze_temps(temps)
display_analysis(result[0], result[1], result[2])
