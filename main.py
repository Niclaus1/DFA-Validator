import re

def get_pattern_code():
    print("""
    OPTIONS:
    1  = single 1
    0  = single 0
    1* = infinite 1s (0 or more)
    0* = infinite 0s (0 or more)
    e1 = consecutive even pair of 1s (11, 1111...)
    e0 = consecutive even pair of 0s (00, 0000...)
    o1 = consecutive odd 1s (1, 111...)
    o0 = consecutive odd 0s (0, 000...)
    """)
    
    user_input = input("Create your Pattern (use ',' to separate): ")
    parts = user_input.split(",")
    
    # Build the regex string directly (Skip the intermediate 'code numbers')
    regex_pattern = "^" # Start of string
    
    pattern_map = {
        "1": "1",
        "0": "0",
        "1*": "1*",
        "0*": "0*",
        "e1": "(11)*",
        "e0": "(00)*",
        "o1": "1(11)*",
        "o0": "0(00)*"
    }

    for part in parts:
        part = part.strip() # Remove accidental spaces
        if part in pattern_map:
            regex_pattern += pattern_map[part]
        else:
            print(f"Warning: '{part}' is not a valid code. Skipping.")

    regex_pattern += "$" # End of string
    return regex_pattern

def get_test_strings():
    inputs = []
    print("\nType strings to test (type 'stop' to finish):")
    while True:
        val = input("> ")
        if val.lower() == "stop":
            break
        inputs.append(val)
    return inputs

def main():
    # 1. Get the Rules
    final_regex = get_pattern_code()
    print(f"\nGenerated Regex Engine: {final_regex}")
    
    # 2. Get the Test Data
    test_strings = get_test_strings()
    
    # 3. Run the Validator
    print("-" * 20)
    for string in test_strings:
        if re.fullmatch(final_regex, string):
            print(f"'{string}' -> VALID")
        else:
            print(f"'{string}' -> INVALID")
    print("-" * 20)

# Run the program

main()