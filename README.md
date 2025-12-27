# DFA Validator

A Python-based tool that allows users to define custom string patterns using a shorthand syntax and validate input strings against those patterns. While conceptually based on Deterministic Finite Automata (DFA), this tool leverages Python's robust Regular Expression engine for validation.

## Features

- **Custom Pattern Creation**: Build complex patterns by combining simple building blocks.
- **Batch Validation**: Test multiple strings in a single session.
- **Instant Feedback**: Immediately see if a string is `VALID` or `INVALID` based on your rules.

## How to Run

1. Ensure you have Python installed.
2. Run the script in your terminal:
   ```bash
   python main.py
   ```

## Usage Guide

### 1. Define a Pattern
When prompted, enter a sequence of codes separated by commas.

**Available Codes:**

| Code | Meaning | Example Match |
|------|---------|---------------|
| `1`  | Single '1' | `1` |
| `0`  | Single '0' | `0` |
| `1*` | Infinite '1's (Zero or more) | `""`, `1`, `111` |
| `0*` | Infinite '0's (Zero or more) | `""`, `0`, `000` |
| `e1` | Even number of '1's | `""`, `11`, `1111` |
| `e0` | Even number of '0's | `""`, `00`, `0000` |
| `o1` | Odd number of '1's | `1`, `111`, `11111` |
| `o0` | Odd number of '0's | `0`, `000`, `00000` |

**Example Input:**
```text
1, 0*, e1
```
*This pattern means: A single '1', followed by any number of '0's, followed by an even number of '1's.*

### 2. Test Strings
Enter the strings you want to validate one by one. Type `stop` when you are finished.

**Example Session:**
```text
> 10011
> 111
> stop
```

### 3. View Results
The program will output the validation status for each string.

```text
'10011' -> VALID
'111' -> INVALID
```
