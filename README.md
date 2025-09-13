# Bitwise Calculator 🔢

An interactive calculator for performing bitwise operations on binary strings and numbers with step-by-step visualization.

## 📋 Features

- **Bitwise operations**: AND (`&`), OR (`|`), XOR (`^`)
- **Shift operations**: LEFT SHIFT (`<<`), RIGHT SHIFT (`>>`)
- **Automatic conversion**: supports various input data types
- **Step-by-step output**: detailed display of each bitwise operation step
- **Smart processing**: automatic operand length alignment


## Installation

```bash
git clone https://github.com/Sarmatae685/Bitwise-Calculator.git
cd Bitwise-Calculator
python3 Bitwise\ Calculator.py
```

## Usage

```shell
# Run the program
python3 Bitwise\ Calculator.py

# Enter operands
Input 1st operand (x): 0011
Input 2st operand (y): 0101

# Select operation
Available options: & | ^ << >>
Your choice: ^
```

## Usage Examples

### XOR Bitwise Operation
```shell
# Input operands
Input: x = '0011', y = '0101'
Operation: <<

# Example XOR output
== ^ Bit by bit operation==
Final operands:
x = 0011
y = 0101
step 0: 0 ^ 0 --> 0
step 1: 0 ^ 1 --> 1
step 2: 1 ^ 0 --> 1
step 3: 1 ^ 1 --> 0
result: 0110

result1: 0110
```

### Left Shift Operation
```
# Input operands
Input: x = '001100000', y = '2'
Operation: <<

# Example Left Shift output
== << Shift operation ==
x should be converted to int for shift operation
y should be int (number of positions to shift)

x = '001100000' (binary) → 96 (decimal)
y = '2' → 2 (shift positions)
001100000(96) << 2
110000000(384)

result1: 384
```

## 🔧 Supported Input Formats

### Bitwise Operations (&, |, ^)
- **Binary strings**: `'1010'`, `'0011'`
- **Decimal strings**: `'123'` → automatically converts to binary

**Note**: Strings containing only 0s and 1s (like `'10'`, `'01'`) are treated as binary strings, not decimal numbers.

### Shift Operations (<<, >>)
- **x (first operand)**:
  - Binary string: `'1010'` → converts to number `10`
  - Decimal string: `'123'` → converts to number `123`
  - Number: `10` → used as is
- **y (second operand)**: number of positions to shift
  - Binary string: `'1010'` → converts to `10` positions  
  - Decimal string: `'123'` → converts to `123` positions
  - Number: `10` → `10` positions

**Note**: Strings containing only 0s and 1s are treated as binary strings in both operands.


## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/Sarmatae685)
