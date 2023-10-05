import calendar

# Get user input for year and month
year = int(input("Enter year (e.g., 2023): "))
month = int(input("Enter month (1-12): "))

# Validate the input
if year < 1 or month < 1 or month > 12:
    print("Invalid input. Please enter a valid year and month.")
else:
    # Create a calendar object
    cal = calendar.month(year, month)

    # Display the calendar
    print("\nCalendar for {} - {}\n".format(calendar.month_name[month], year))
    print(cal)
