# NOTE: in use is invert_v3() function

def invert_v1(number, width=8): 
    '''Version 1 - static width'''
    result = ~number

    result_binary = bin(result) # 0b or -0b

    if '-' in str(result):
        print(f"~{number} = {result}")  # ~5 = -6
        print(f"{result_binary[3:]}({result})") # slice -0b from result of invert(5) call = -0b110(-6)
    else:
        print(f"~({number}) = {result}")  # ~(-5) = 4
        print(f"{result_binary[2:]}({result})") # slice 0b from result of invert(-5) call = 0b100(4)


def invert_v2(number, width=8):
    '''Version 2 - Added mask for 2's compliment representation'''
    result = ~number
    # Convert the number to an unsigned representation within the bit width (Create a mask to limit to the bit width)
    mask = (1 << width) - 1  # For 8 bit: 0b11111111 (255)
    # We get an unsigned representation of the bit pattern
    # Next, apply the mask
    result_mask = result & mask # for -6 get 250, for -22 --> 234 (identical bit pattern)

    if result < 0: # for example: ~5 = -6
        print(f"~{number} = {result}")
        # For a negative result, we show the full binary representation (mask required)
        result_binary = bin(result_mask)[2:].zfill(width)
        print(f"two's compliment: \n"
              f"{result_binary}({result} or {result_mask})")
    else: # ~(-5) = 4
        print(f"~({number}) = {result}") # if the "result" is positive, then "number" is negative
        result_binary = bin(result)[2:].zfill(width)
        print(f"{result_binary}({result})")


def invert_v3(number):
    result = ~number
    '''Version 3 - added automatic bit representation width definition'''
    # Automatically detect width based on a number
    if number == 0:
        width = 8
    elif number > 0:
        width = max(8, number.bit_length())
    else:  # number < 0
        # For negative numbers, an additional bit is required for the sign
        width = max(8, abs(number).bit_length() + 1)

    # Create a mask to limit to bit width
    mask = (1 << width) - 1
    result_mask = result & mask

    if result < 0:
        print(f"~{number} = {result}")
        result_binary = bin(result_mask)[2:].zfill(width)
        print(f"two's complement ({width}-bit): \n{result_binary}({result} or {result_mask})")
    else:
        print(f"~({number}) = {result}")
        result_binary = bin(result)[2:].zfill(width)
        print(f"two's complement ({width}-bit): \n{result_binary}({result})")


# test
# invert_v3(-5)
# invert_v3(21834578)
# invert_v3(-9678380976)


