def bitwise_operation(*numbers, operation='^'):
    if len(numbers) < 2:
        raise ValueError("At least 2 numbers are required for the operation")

    operations = {
        '&': lambda x, y: x & y,
        '|': lambda x, y: x | y,
        '^': lambda x, y: x ^ y
    }
    # check if the "operation" parameter is in the "operations" dict
    if operation not in operations:
        raise ValueError(f"Unknown operation {operation}. Available operations: {key}" for key in operations.keys())

    operation_to_do = operations[operation] # call lambda function by "operation" key!

    # run a loop through all the passed parameters in "*numbers", and look for the longest of their binary representations
    length_of_longest_binary = max(len(bin(num)[2:]) for num in numbers)

    print('Input values: ')
    binary_nums_padded = [bin(num)[2:].zfill(length_of_longest_binary) for num in numbers]

    # print the binary number and its int form
    print(', '.join([f"{binary}({int_form})" for (binary, int_form) in zip(binary_nums_padded, numbers)]))
    print()

    # calculate XOR
    starting_operand = numbers[0]
    for num_to_do in numbers[1:]:  # ← Start with index 1
        #starting_operand ^= num_to_do # otherwise, it will turn out that XOR will be performed twice for numbers[0]:  numbers[0] ^ numbers[0] ^ numbers[1]...
        starting_operand = operation_to_do(starting_operand, num_to_do) # here is --> operation_to_do = lambda x, y: x ^ y

    expression = f" {operation} ".join(str(num) for num in numbers)
    print(f"{expression} = {starting_operand}")
    print()

    # Bitwise computation
    result_binary = ""
    for bit_pos in range(length_of_longest_binary):
        bits = [binary_nums_padded[i][bit_pos] for i in range(len(numbers))]

        bit_result = int(bits[0])
        for i in range(1, len(bits)):
            # bit_result ^= int(bits[i]) --> option before I added dict with lambda functions
            bit_result = operation_to_do(bit_result, int(bits[i]))

        result_binary += str(bit_result)
        bits_str = f" {operation} ".join(bits) # join by passed "operation" symbol (operation)
        print(f"{bits_str} = {bit_result}")

    manual_result = int(result_binary, 2)
    print(f"Result: {result_binary} ({manual_result})")


# test
# bitwise_operation(23, operation='&') # видасть ValueError
# bitwise_operation(23, 5, operation='|')

# bitwise_operation(23, 5, operation='^')
