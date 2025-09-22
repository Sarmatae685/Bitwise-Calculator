def shift(number, shift_value, operator='<<'):
    # check that will raise an error if shift_value is NOT an int() or shift_value is True/False (so that they are not treated as 1/0)
    if not isinstance(shift_value, int) or isinstance(shift_value, bool):
        raise ValueError(f'shift_value must be int(), not {type(shift_value).__name__}')

    # Check for negative values
    if shift_value < 0:
        raise ValueError('shift_value can\'t be negative!')

    operations = {
        '<<': lambda x, y: x << y,
        '>>': lambda x, y: x >> y
    }
    if operator not in operations:
        raise ValueError(f"Unknown operator: {operator}")

    # pass the action <<, >>
    operation_to_do = operations[operator]

    # operations on numbers
    result = operation_to_do(number, shift_value)  # here it'll be --> result = lambda x, y: x <</>> y
    print(f"{number} {operator} {shift_value} = {result}")

    # bitwise conversion
    '''
    1. number will be padded to 8 bits (input value)                                  
    2. if len(after_shift) >= 8, then print after_shift as it is, without padding (shift operator will pad it automatically)
    3. Else if len(after_shift) < 8, then print after_shift.zfill(8)

    << - adds zeros to the right automatically
    >> - "eats" bits on the right, they disappear
    '''

    length_to_be_printed = 8

    number_binary = bin(number)[2:].zfill(length_to_be_printed)
    print(f"Input: {number_binary}({number}) {operator} {shift_value}")

    after_shift = bin(result)[2:]
    if len(after_shift) >= 8:
        print(f"Output: {after_shift}({result})\n")
    else:
        print(f"Output: {after_shift.zfill(length_to_be_printed)}({result})\n")

# test
# shift(23, 1)
# shift(23, 0, '<<')
# shift(23, 2, '>>')
