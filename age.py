from datetime import datetime


def main():
    # Get todays date, set time to 00
    current_date = datetime.today().replace(hour=0,
                                            minute=0,
                                            second=0,
                                            microsecond=0)

    # Get user input
    previous_date = input("Please enter a date (in the format DD-MM-YYYY): ")
    # Parse date
    previous_date = datetime.strptime(previous_date, "%d-%m-%Y")

    # If the date entered is in the future then ignore
    if (previous_date >= current_date):
        print(
            "ERROR! Cannot calculate age as the date you entered is in the future!"
        )
    else:
        # Calculate the differences in dates
        time_delta = current_date - previous_date
        # Divide by 365 to find the year
        years = time_delta.days // 365
        # Print the output
        print(f"The age is {years} Years")


if __name__ == '__main__':
    main()
