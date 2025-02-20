import re
import pandas as pd

KEYWORDS = {"int": "KW_INT", "if": "KW_IF"}
OPERATORS = {"=": "SYM_EQUAL", "+": "SYM_PLUS", "-": "SYM_MINUS", "*": "SYM_MULT", "/": "SYM_DIV"}
RELATIONAL_OPERATORS = {">": "SYM_GT", "<": "SYM_LT", ">=": "SYM_GTE", "<=" : "SYM_LTE"}
SYMBOLS = {";": "SYM_PV", "{": "SYM_LBRACE", "}": "SYM_RBRACE", "(": "SYM_LPAREN", ")": "SYM_RPAREN"}

TOKEN_REGEX = r"\bint\b|\bif\b|\w+|[=+\-*/><{}();]"

def tokenize(code):
    tokens = []
    tokenized_array = []
    token_id = 1
    
    matches = re.findall(TOKEN_REGEX, code)
    
    for match in matches:
        if match in KEYWORDS:
            token_type = KEYWORDS[match]
            value = "-"
        elif match in OPERATORS:
            token_type = OPERATORS[match]
            value = "-"
        elif match in RELATIONAL_OPERATORS:
            token_type = RELATIONAL_OPERATORS[match]
            value = "-"
        elif match in SYMBOLS:
            token_type = SYMBOLS[match]
            value = "-"
        elif match.isdigit():
            token_type = "NUMBER"
            value = match
        else:
            token_type = "ID"
            value = "-"
        
        tokens.append((token_id, match, token_type, value))
        tokenized_array.append(f"<{token_type}, {token_id}>")
        token_id += 1
    
    return tokens, tokenized_array

code = """
int a = 134;
int b = 23;
if(b > 30)
    int c = b + a;
if(a > 100) {
    int c = a - b;
    int d = a * a + c;
}
"""

tokens, tokenized_array = tokenize(code)

df = pd.DataFrame(tokens, columns=["id", "lexema", "token", "valor"])
print(df)

tokenized_output = " ".join(tokenized_array)
print("Código Tokenizado:", tokenized_output)
