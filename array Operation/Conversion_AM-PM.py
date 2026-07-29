import re

def timeConversion(s):
    # Regular expression to match the valid time format
    valid_time_pattern = re.compile(r'^(0[1-9]|1[0-2]):([0-5][0-9]):([0-5][0-9])(AM|PM)$')

    # Check if the input matches the valid time format
    if not valid_time_pattern.match(s):
        return "Invalid time format"

    # Extract the period (AM/PM)
    period = s[-2:]
    # Extract the hour part
    hour = int(s[:2])
    # Extract the rest of the time (minutes and seconds)
    rest_of_time = s[2:-2]

    # Convert hour based on AM/PM period
    if period == "AM":
        if hour == 12:
            hour = 0
    else:  # PM case
        if hour != 12:
            hour += 12

    # Format the new hour to be two digits
    new_hour = f"{hour:02}"

    # Return the new formatted time
    return f"{new_hour}{rest_of_time}"

# Main block to execute the function
if __name__ == '__main__':
    s = input("Enter the time in 12-hour format (e.g., 07:05:45PM): ").strip()
    result = timeConversion(s)
    if result == "Invalid time format":
        print(result)
    else:
        print(f"Converted time in 24-hour format: {result}")
