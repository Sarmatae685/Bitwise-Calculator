def get_numbers_for_bitwise(operation=None):
    name_to_print = 'AND' if operation == '&' else 'OR' if operation == '|' else 'XOR' if operation == '^' else None

    while True:
        user_input = input(f"Enter numbers for {name_to_print} separated by a space (type 'exit' for exit): ")  # str

        if user_input.lower().strip() == 'exit':
            print('See ya!')
            exit(1)
        try:
            numbers = [int(num.strip()) for num in user_input.split()]
            if len(numbers) < 2:
                print("At least 2 numbers required! Enter again...")
                continue

            return numbers
        except ValueError:
            print("Error: enter only space-separated integers!")
            continue


def get_numbers_for_shift(operation=None):
    name_to_print = 'to the LEFT' if operation == '<<' else 'to the RIGHT' if operation == '>>' else None

    while True:
        user_input = input(f"enter number to shift {name_to_print} by how many bits to shift"
                           f"(example: 23 5) or type 'exit' for exit: ").strip()

        if user_input.lower() == 'exit':
            print('See ya!')
            exit(1)

        try:
            values = user_input.split()

            if len(values) != 2:
                print("You need to enter exactly 2 numbers separated by a space!")
                continue

            number = int(values[0])
            shift_value = int(values[1])

            return [number, shift_value]

        except ValueError:
            print(f"Error: '{user_input}' contains non-numeric values. Please, try again...")


def get_number_for_invert():
    while True:
        input_number = input("Enter number to invert (type 'exit' to exit): ")
        if input_number.lower().strip() == 'exit':
            print('See ya!')
            exit(1)
        try:
            return int(input_number)
        except ValueError:
            print(f"Can't convert {input_number} to int(). Enter again...")
