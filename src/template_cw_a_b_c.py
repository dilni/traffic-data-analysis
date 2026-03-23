#Author: 
#Date: 
#Student ID: 

# Task A: Input Validation
def validate_date_input():
    """
    Prompts the user for a date in DD MM YYYY format, validates the input for:
    - Correct data type
    - Correct range for day, month, and year
    """
    while True:
        try:
            # Ask user to input the date
            user_input_date = input("Enter the date in DD MM YYYY format: ")

            # Replace common separators (., /, -) with spaces for easier processing
            user_input_date = user_input_date.replace('.', ' ').replace('/', ' ').replace('-', ' ').replace(',', ' ')

            # Split the input into parts
            parts = user_input_date.split()
            
             # Ensure that the parts are integers (day, month, year)
            if not all(part.isdigit() for part in parts):
                print("Invalid input. Only integers are allowed for day, month, and year.")
                continue
            
            if len(parts) != 3:
                print("Invalid format. Please enter the date as DD MM YYYY.")
                continue

            # Convert the parts to integers (day, month, year)
            day, month, year = map(int, parts)
            '''for split can use build-up function like 'map' to cover whole datasets and make the code clear more. day, month, year = map(int, date_input.split())'''

            # Debugging: Show day, month, year values
            print(f"Day: {day}, Month: {month}, Year: {year}")
                
            # Validate year range
            if not (2000 <= year <= 2024):
                print("Invalid year. Please enter a year between 2000 and 2024.")
                continue

            # Validate month range
            if not (1 <= month <= 12):
                print("Invalid month. Must be between 1 and 12. Try again.")
                continue #use this to skip the remaining code.if not use this code will continue with invalid input

            # Validate day range
            if not (1 <= day <= 31):
                print("Invalid day. Must be between 1 and 31. Try again.")
                continue

            # Check for months with only 30 days
            if month in {4, 6, 9, 11} and day > 30:
                print(f"Invalid day. Month {month} only has 30 days. Try again")
                continue
            
            '''#handel february month(finding that the year is leap year or not)
               # method of find the year is leap or not
               # 1. year%4==0
               # 2. year%100!=0
               # 3. year%400==0'''
            # Check February (leap year consideration)
            if month == 2:
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):  # Leap year
                    if day > 29:
                        print("Invalid day. February has only 29 days in a leap year.")
                        continue
                else:  # Not a leap year
                    if day > 28:
                        print("Invalid day. February has only 28 days in a non-leap year.")
                        continue

            # If all checks pass, the date is valid
            print(f"Valid date: {day:02}-{month:02}-{year}")
            return day, month, year  # Return the date as a tuple

        except ValueError:
            print("Invalid input. Please enter the date as DD MM YYYY.")

# Call the function to execute it
validate_date_input()

def validate_continue_input():
    """
    Prompts the user to decide whether to load another dataset:
    - Validates "Y" or "N" input
    """
     while True:
        user_input = input("Do you want to open another Excel file? (Y/N): ").strip().upper()
        
        if user_input == 'Y':
            return True  # User wants to continue (open another file)
        
        elif user_input == 'N':
            return False  # User wants to stop the program
        
        else:
            print("Invalid input. Please enter 'Y' for Yes or 'N' for No.")

def main():
    while True:
        # Step 1: Ask if the user wants to load another file
        continue_program = validate_continue_input()
        
        if continue_program:
            # Continue to the next iteration (open another file or re-run)
            print("Processing the next file...\n")
            continue
        else:
            # Exit the loop
            print("Exiting the program. Goodbye!")
            break

# Start the program
main()



# Task B: Processed Outcomes
def process_csv_data(file_path):
    """
    Processes the CSV data for the selected date and extracts:
    - Total vehicles
    - Total trucks
    - Total electric vehicles
    - Two-wheeled vehicles, and other requested metrics
    """
    pass  # Logic for processing data goes here

def display_outcomes(outcomes):
    """
    Displays the calculated outcomes in a clear and formatted way.
    """
    pass  # Printing outcomes to the console


# Task C: Save Results to Text File
def save_results_to_file(outcomes, file_name="results.txt"):
    """
    Saves the processed outcomes to a text file and appends if the program loops.
    """
    pass  # File writing logic goes here

# if you have been contracted to do this assignment please do not remove this line
