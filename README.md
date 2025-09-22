# 📱Bitwise Calculator

A comprehensive command-line calculator for bitwise operations, bit shifting, and logical inversion. This educational tool provides detailed step-by-step calculations and binary representations for better understanding of bitwise operations.

## ⚙️Features
### 0️⃣1️⃣ Bitwise Operations
- AND (`&`) - Logical AND operation between multiple numbers
- OR (`|`) - Logical OR operation between multiple numbers
- XOR (`^`) - Exclusive OR operation between multiple numbers

### ⏪⏩ Bit Shifting
- Left Shift (`<<`) - Shifts bits to the left by specified positions
- Right Shift (`>>`) - Shifts bits to the right by specified positions

### 🔄 Bit Inversion
- NOT (`~`) - Bitwise inversion with automatic width detection and two's complement representation

## ⬇️ Installation
1. Clone the repository:
```bash
git clone https://github.com/Sarmatae685/src.git
cd src
```
2. Run the program:
```bash
python3 main.py
``` 

## 📌Examples
### Bitwise XOR Operation
```
Enter an action from the following  &  |  ^  <<  >>  ~ : ^
Selected action: ^
This is a Bitwise operation, requires at least 2 operands: x1 ^ x2...
Enter numbers for XOR separated by a space (type 'exit' for exit): 12 7 3
Input values: 
1100(12), 0111(7), 0011(3)

12 ^ 7 ^ 3 = 8

1 ^ 0 ^ 0 = 1
1 ^ 1 ^ 0 = 0
0 ^ 1 ^ 1 = 0
0 ^ 1 ^ 1 = 0
Result: 1000 (8)
```
### Bit Shifting
```
Enter an action from the following  &  |  ^  <<  >>  ~ : <<
Selected action: <<
This is a shift operation, requires 2 operands: num << steps to shift
enter number to shift to the LEFT by how many bits to shift(example: 23 5) or type 'exit' for exit: 5 4
5 << 4 = 80
Input: 00000101(5) << 4
Output: 01010000(80)
```
### Bit Inversion
```
Enter an action from the following  &  |  ^  <<  >>  ~ : ~
Selected action: ~
This is logical NOT: ~x = -(x + 1)
Enter number to invert (type 'exit' to exit): 5
~5 = -6
two's complement (8-bit): 
11111010(-6 or 250)
```

## 📁 Project Structure
```
bitwise-calculator/
├── main.py                 # Main program logic and menu
├── bitwise_operations.py   # Bitwise AND, OR, XOR operations
├── bit_shift.py            # Left and right bit shifting
├── bit_inversion.py        # Bitwise NOT operation
└── input_handlers.py       # Input validation and user interaction
```

## ⚙️ Key Features
### Smart Input Validation

- Flexible operator input: Accepts multiple consecutive operators (e.g., &&&& → &)
- Robust error handling: Validates numeric inputs and operation parameters
- User-friendly prompts: Clear instructions and error messages

### Detailed Binary Visualization

- Step-by-step calculation: Shows bit-by-bit operation process
- Automatic width detection: Adjusts binary representation width based on input numbers
- Two's complement support: Proper handling of negative numbers in bit inversion

### 🧾 License
This project is open source and available under the MIT License.
