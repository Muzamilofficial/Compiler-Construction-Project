import sys
from your_scanner_file_name import Scanner, GeneratedScanner

# Your CFG rules here
# You can define the rules as needed for your language

# Modified CFG rules based on your requirements
CFG_RULES = {
    "DS": 'TBVO',
    "T": 'int|float|char|string|bool',
    "B": 'bB|b',
    "V": 'XY',
    "L": 'A|B|...|Z|a|b|...|z',
    "D": '0|1|2|...|9',
    "X": '-L',
    "Y": '-Y|LY|DY|^',
    "S": 'aS|bS|^',
    "O": 'i|,VO|=WO',
    "W": 'N|-N|N.N|\'C\'|"S"|BL|V|E|F|10',
    "N": 'DN|D',
    "C": '0|1|...|9|A|...|a|...|+|-|(|}|...|...)',
    "BL": 'True|False'
}

# Function to validate code against CFG
def validate_code(declarative_code):
    # Initialize the scanner
    scanner = Scanner()

    # Tokenize the declarative code
    for line in declarative_code.split('\n'):
        scanner.tokenize(line)

    # Validate tokens against CFG
    valid_tokens = []
    for token in scanner.tokens:
        if token.type == Scanner.TokenType.Comment:
            continue  # Ignore comments for validation

        # Validate token based on CFG
        validation_result = GeneratedScanner.__dict__[token.type].match(token.value) is not None
        valid_tokens.append((token, validation_result))

    return valid_tokens, all(result[1] for result in valid_tokens)

# Read the contents of read.py
with open(sys.argv[0], 'r') as file:
    declarative_code = file.read()

# Validate code against CFG
validation_result, is_code_valid = validate_code(declarative_code)

print("\nValidation Result:")
for token, valid in validation_result:
    print(f'Token: {token}, Valid: {valid}')

print("\nCode is valid according to CFG:", is_code_valid)
