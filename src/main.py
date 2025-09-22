from bitwise_operations import bitwise_operation
from bit_shift import shift
from bit_inversion import invert_v3
from input_handlers import get_numbers_for_bitwise, get_numbers_for_shift, get_number_for_invert
import re

def print_menu():
    print("Bitwise operations:\n"
          "& - AND\n"
          "| - OR\n"
          "^ - XOR\n"
          "Shift:\n"
          "<< - Left\n"
          ">> - Right\n"
          "Invert:\n"
          "~ - NOT\n")

def validate_operator(_operator):
    """
    Validating "_operator" using regular expressions
    Handles situations, such as:
    '&&&&&&&&&&&&...' will return '&'
    '||||||||||||||...' will return '|'
    '<<<<<<<<<<<<<...' will return '<<'
    '>>>>>>>>>>>>...' will return '>>'
    ...
    """

    # Check for pattern matching
    if re.match(r'^&+$', _operator): # 1 or more &
        return '&'
    elif re.match(r'^\|+$', _operator): # 1 or more | (need to escape \|)
        return '|'
    elif re.match(r'^\^+$', _operator): # 1 or more ^ (need to escape \^ because ^ itself means the beginning of a line)
        return '^'
    elif re.match(r'^<+$', _operator):  # 1 or more < (interpret as <<)
        return '<<'
    elif re.match(r'^>+$', _operator): # 1 or more > (interpret as >>)
        return '>>'
    elif re.match(r'^~+$', _operator): # 1 or more ~
        return '~'
    else:
        return None

def main():
    print_menu()
    input_operator = input('Enter an action from the following  &  |  ^  <<  >>  ~ : ') # will create a list from which we will extract the 0-element below and compare it in the if-elif branch

    # Handling the case when we entered nothing (or entered a lot of spaces) and pressed Enter
    if not input_operator.strip():
        print("You haven't entered anything!")
        exit(2)

    operator = [str(op) for op in input_operator.split()][0] # separate by spaces using the split() method and save only the [0]-element for comparison
    # validated_operator
    v_operator = validate_operator(operator) #  to filter '<<<<<...' or '||||...' and so on.

    # Handling the case when validate_operator() returned None
    if v_operator is None:
        print(f"Unknown operation: '{operator}'. Available operations: &, |, ^, <<, >>, ~")
        exit(2)

    print(f"Selected action: {v_operator}")

    if v_operator in '&|^':
        print(f"This is a Bitwise operation, requires at least 2 operands: x1 {v_operator} x2...")
        values = get_numbers_for_bitwise(v_operator)
        bitwise_operation(*values,operation=v_operator) # specify the parameter explicitly, because PyCharm cannot understand where *numbers ends

    elif v_operator in ['<<', '>>']:
        print(f"This is a shift operation, requires 2 operands: num {v_operator} steps to shift")
        number, shift_value = get_numbers_for_shift(v_operator) # Python will automatically unpack returned "values_to_return"
        shift(number, shift_value, v_operator)

    elif v_operator == '~':
        print(f"This is logical NOT: {v_operator}x = -(x + 1)")
        num = get_number_for_invert()
        invert_v3(num)


if __name__ == "__main__":
    main()
