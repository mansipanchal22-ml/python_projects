# input data
lst = []
def inputArray(lst):
    userInput = int(input("Enter type of Array: "))

    match userInput:

        case 1:
            lst = list(map(int, input("Enter the value by space: ").split()))
            return lst

        case 2:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))

            values = rows * cols

            for i in range(rows):
                lsts = list(map(int, input(
                    f"Enter the value {values} by space: "
                ).split()))

                lst.append(lsts)

            return lst

lst = inputArray(lst)
print(lst)

# data summary
def dataSummary(lst):

    singlelist = []

    for row in lst:
        if isinstance(row, list):
            singlelist.extend(row)
        else:
            singlelist.append(row)

    return f'''
    Data Summary:
    - Total Element: {len(singlelist)}
    - Minimum value: {min(singlelist)}
    - Maximum value: {max(singlelist)}
    - Sum of all Value: {sum(singlelist)}
    - Average value: {sum(singlelist) / len(singlelist)}
    '''

print(dataSummary(lst))


# factorial
def factorial(no):                                      # ⭐ CHANGED
    """
    Factorial:UDF to calculate factorial using recursion
    """

    def fact(no):

        if no == 0 or no == 1:
            return 1
        else:
            return no * fact(no - 1)

    result = fact(no)
    print(f"Factorial of {no} is : {result}")


# filter data
def filter_data():
    """
    Filter data using lambda function.
    """

    if not lst:
        print("No data available to filter.")
        return

    print("Choose filtering option:")
    print("1. Get numbers greater than a threshold")
    print("2. Get numbers less than a threshold")
    print("3. Get even numbers")

    choice = int(input("Enter choice: "))

    singlelist = []

    for row in lst:
        if isinstance(row, list):
            singlelist.extend(row)
        else:
            singlelist.append(row)

    if choice == 1:

        threshold = int(input("Enter threshold value: "))

        filtered = list(
            filter(lambda x: x >= threshold, singlelist)
        )

        print(f"Numbers greater than {threshold}: {filtered}")

    elif choice == 2:

        threshold = int(input("Enter threshold value: "))

        filtered = list(filter(lambda x: x <= threshold, singlelist))

        print(f"Numbers less than {threshold}: {filtered}")

    elif choice == 3:

        filtered = list(
            filter(lambda x: x % 2 == 0, singlelist)
        )

        print(f"Even numbers: {filtered}")

    else:
        print("Invalid choice.")


# sort data
def sortted():
    """sortted:Sorted data in ascending or descending order."""

    if not lst:
        print("Not available")
        return

    print("""
    Choose sorting option:
    1. Ascending
    2. Descending
    """)

    choice = int(input("Enter your choice: "))

    singlelist = []

    for row in lst:
        if isinstance(row, list):
            singlelist.extend(row)
        else:
            singlelist.append(row)

    if choice == 1:

        sorted_data = sorted(singlelist)

        print(f"Sorted Data in Ascending order: {sorted_data}")

    elif choice == 2:

        sorted_data = sorted(singlelist, reverse=True)

        print(f"Sorted Data in Descending order: {sorted_data}")
    else:
        print("Invalid choice")

# statistics
def statistics(**kwargs):
    """
    ==============
    Statistics:
    ==============
    UDF to process dataset statistics using keyword arguments.
    """
    dataset = kwargs.get('Dataset', [])

    if not dataset:
        print("The dataset is empty.")
        return None, None, None, None, None

    singlelist = []

    for row in dataset:
        if isinstance(row, list):
            singlelist.extend(row)
        else:
            singlelist.append(row)

    tot_ele = len(singlelist)
    min_val = min(singlelist)
    max_val = max(singlelist)
    total_sum = sum(singlelist)
    average_val = total_sum / tot_ele

    print("Dataset summary using **kwargs:")

    for key, value in kwargs.items():
        print("-", key, ":", value)

    print("-- calculate dataset statistics --")

    print(f"Count: {tot_ele}")
    print(f"Min: {min_val}")
    print(f"Max: {max_val}")
    print(f"Sum: {total_sum}")
    print(f"Average: {average_val}")

    return (
        tot_ele,
        min_val,
        max_val,
        total_sum,
        average_val
    )

# Main Program

print("Welcome to the Data Analyzer and Transformer program")

while True:

    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary(Built-in-Functions)")
    print("3. Calculate Factorial(Recursion)")
    print("4. Filter Data by Threshold(Lambda Function)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics(Return Multiple Values)")
    print("7. Exit Program")

    user_choice = int(input("Please enter your choice: "))

    if user_choice == 1:

        lst = inputArray(lst)
        print(lst)
        print("Data has been stored successfully!")

    elif user_choice == 2:

        if not lst:
            print(
                "Error: No data available. "
                "Please select option 1 first."
            )
        else:
            print(dataSummary(lst))

    elif user_choice == 3:

    
        no = int(
            input(
                "Enter a number to calculate its factorial: "
            )
        )
        factorial(no)

    elif user_choice == 4:
        filter_data()
    elif user_choice == 5:
        sortted()
    elif user_choice == 6:

        if not lst:
            print(
                "Error: No data available. "
                "Please select option 1 first.")
        else:
            statistics(Dataset=lst)

    elif user_choice == 7:

        print(
            "Thank you for using the Data Analyzer "
            "and Transformer program. Goodbye!")
        break
    else:

        print("Invalid Choice. Option in (1 to 7)")