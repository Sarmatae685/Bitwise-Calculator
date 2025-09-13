def is_binary_string(s):
    if not isinstance(s, str):
        return False # бо цей метод дивиться, чи це РЯДОК, і чи він БІНАРНИЙ, тому int тут не приймається
    return all(char in '01' for char in s) and len(s) > 0 #щоб рядок складався з 0,1 і не був порожній водночас


def to_binary_string(value, estimated_length):
    if isinstance(value, str):
        # якщо вже рядок, перевіряємо, чи бінарний
        if is_binary_string(value):
            return value # рядок вже відповідає умовам і перетворювати його не треба
        else:
            # якщо рядок наприклад '123', то перетворимо в бінарний і доповнимо до переданої довжини
            num = int(value)
            binary_value = bin(num)[2:].zfill(estimated_length)
            return binary_value
    elif isinstance(value, int):
        # якщо це int, то треба конвертувати в binary
        binary = bin(value)[2:] # bin() завжди повертає str
        return binary.zfill(estimated_length)
    else:
        print(f"The following {type(value)} is not supported!\n")
        return 1

def print_variables(_x, _y):
    print(f"x = {x}\n"
          f"y = {y}")


def bitwise_operation(x, y):
    operations = {
        '&': lambda x, y: x & y,
        '|': lambda x, y: x | y,
        '^': lambda x, y: x ^ y,
        '<<': lambda x, y: x << y,
        '>>': lambda x, y: x >> y
    }

    original_length = max(len(x), len(y))
    print_variables(x, y)

    print("Available options: & | ^ << >>\n")
    choose = input("Your choice: ")

    if choose not in operations:
        print('Unknown operation')
        return 2

    if choose in ['&', '|', '^']:
        print(f'== {choose} Bit by bit operation==')

        # оскільки ми рахуємо довжину ДО перевірки, чи x, y є бінарними, то ми переводимо їх в str
        # це потрібно, оскільки може бути передано x = 10, y = '1010', а int не має len!
        target_length = max(len(str(x)), len(str(y)))

        if not is_binary_string(x):
            print(f"!! x = {x} is not binary string!")
            print(f'Transforming {x}...')
            x = to_binary_string(x, target_length)
            print(f"{x} is binary now!")

        if not is_binary_string(y):
            print(f"!! y = {y} is not binary string!")
            print(f'Transforming {y}...')
            y = to_binary_string(y, target_length)
            print(f"{y} is binary now!")

        # Додаткове вирівнювання після конвертації
        final_length = max(len(x), len(y))
        x = x.zfill(final_length)
        y = y.zfill(final_length)

        print(f'Final operands:\n'
              f'x = {x}\n'
              f'y = {y}')

        result = ''
        for i, (bit1, bit2) in enumerate(zip(x, y)):

            bit1_int = int(bit1)
            bit2_int = int(bit2)

            output_bit = operations[choose](bit1_int, bit2_int)
            print(f"step {i}: {bit1} {choose} {bit2} --> {output_bit}")
            result += str(output_bit)

        print(f"result: {result}")
        return result

    # Зсуви - це операції над цілими числами, не побітові
    elif choose in ['<<', '>>']:
        print(f'== {choose} Shift operation ==')
        print('x should be converted to int for shift operation')
        print('y should be int (number of positions to shift)\n')


        if isinstance(x, str) and is_binary_string(x):
            original_x_length = len(x)
            x_int = int(x, 2) # Бінарний рядок → число
            print(f"x = '{x}' (binary) → {x_int} (decimal)")
        else:
            # x не бінарний рядок, конвертуємо в десяткове число
            x_int = int(x) # '123' → 123

            # Зберігаємо оригінальну довжину x для форматування результату
            original_x_length = len(bin(x_int)[2:])
            print(f"x = {x} → {x_int} (decimal)")

        if isinstance(y, str):
            y_int = int(y) # десяткове число
            print(f"y = '{y}' → {y_int} (shift positions)")
        else:
            y_int = y
            print(f"y = {y_int} (shift positions)")

        if y_int < 0:
            print(f"Shift on {y_int} may cause problems!!")
            return 3

        result = operations[choose](x_int, y_int) # x: binary string | y: int (на скільки бітів виконувати shift)

        print(f"{x}({x_int}) {choose} {y_int}\n"
              f"{bin(result)[2:].zfill(original_x_length)}({result})")

        return result


x = str(input('Input 1st operand (x): '))
y = str(input('Input 2st operand (y): '))
result1 = bitwise_operation(x, y)
print(f'\nresult1: {result1}')
