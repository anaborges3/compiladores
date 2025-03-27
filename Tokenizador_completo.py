import re
import pandas as pd

PALAVRASCHAVE = { #palavras-chave que o analisador léxico entende
    "auto": "KW_AUTO", 
    "break": "KW_BREAK", 
    "case": "KW_CASE", 
    "char": "KW_CHAR", 
    "const": "KW_CONST", 
    "continue": "KW_CONTINUE", 
    "default": "KW_DEFAULT", 
    "do": "KW_DO", 
    "double": "KW_DOUBLE", 
    "else": "KW_ELSE", 
    "enum": "KW_ENUM", 
    "extern": "KW_EXTERN", 
    "float": "KW_FLOAT", 
    "for": "KW_FOR", 
    "goto": "KW_GOTO", 
    "if": "KW_IF", 
    "inline": "KW_INLINE", 
    "int": "KW_INT", 
    "long": "KW_LONG", 
    "register": "KW_REGISTER", 
    "restrict": "KW_RESTRICT", 
    "return": "KW_RETURN", 
    "short": "KW_SHORT", 
    "signed": "KW_SIGNED", 
    "sizeof": "KW_SIZEOF", 
    "static": "KW_STATIC", 
    "struct": "KW_STRUCT", 
    "switch": "KW_SWITCH", 
    "typedef": "KW_TYPEDEF", 
    "union": "KW_UNION", 
    "unsigned": "KW_UNSIGNED", 
    "void": "KW_VOID", 
    "volatile": "KW_VOLATILE", 
    "while": "KW_WHILE", 
    "_Alignas": "KW_ALIGNAS", 
    "_Alignof": "KW_ALIGNOF", 
    "_Atomic": "KW_ATOMIC", 
    "_Bool": "KW_BOOL", 
    "_Complex": "KW_COMPLEX", 
    "_Generic": "KW_GENERIC", 
    "_Imaginary": "KW_IMAGINARY", 
    "_Noreturn": "KW_NORETURN", 
    "_Static_assert": "KW_STATIC_ASSERT", 
    "_Thread_local": "KW_THREAD_LOCAL"
}

OPERADORES = { #operadores aritméticos e de atribuição
    "=": "SYM_EQUAL", 
    "+": "SYM_PLUS", 
    "-": "SYM_MINUS", 
    "*": "SYM_MULT", 
    "/": "SYM_DIV", 
    "%": "SYM_MOD", 
    "++": "SYM_INCREMENT", 
    "--": "SYM_DECREMENT"
    }

OPERADORES_RELACIONAIS = { #operadores relacionais
    ">": "SYM_GT", 
    "<": "SYM_LT", 
    ">=": "SYM_GTE", 
    "<=" : "SYM_LTE", 
    "==": "SYM_EQ", 
    "!=": "SYM_NEQ"
    }

OPERADORES_LOGICOS = {
    "&&": "SYM_AND", 
    "||": "SYM_OR", 
    "!": "SYM_NOT"
}

BITWISE_OPERATORS = {
    "&": "SYM_BIT_AND", 
    "|": "SYM_BIT_OR", 
    "^": "SYM_BIT_XOR", 
    "~": "SYM_BIT_NOT", 
    "<<": "SYM_LEFT_SHIFT", 
    ">>": "SYM_RIGHT_SHIFT"
}

SIMBOLOS_ESPECIAIS = { #símbolos especiais utilizados
    ";": "SYM_PV", 
    "{": "SYM_LBRACE", 
    "}": "SYM_RBRACE", 
    "(": "SYM_LPAREN", 
    ")": "SYM_RPAREN", 
    "[": "SYM_LBRACKET", 
    "]": "SYM_RBRACKET", 
    ",": "SYM_COMMA", 
    ".": "SYM_DOT", 
    "->": "SYM_ARROW", 
    "?": "SYM_QUESTION", 
    ":": "SYM_COLON"
}

#expressao regular para identificar tokens no código-fonte
REGEX = r"\b(?:" + "|".join(PALAVRASCHAVE.keys()) + r")\b|[a-zA-Z_][a-zA-Z0-9_]*|\d+|[=+\-*/%><!]=?|[&|^~]+|<<|>>|->|[{}();,\[\].?:]"

#Função para tokenizar um código-fonte
#Entrega uma lista de tokens identificados e um array formatado com os tokens
def tokenize(code):
    tokens = [] #array que armazenará os tokens identificados
    tokenized_array = [] #array formatada para exibição dos tokens
    token_id = 1 #id numérico dos tokens
    
    #encontra todos os tokens utilizando a expressão regular
    matches = re.findall(REGEX, code)
    
    #laço e condicionais que determina o tipo do token e seu valor associado
    for match in matches:
        if match in PALAVRASCHAVE:
            token_type = PALAVRASCHAVE[match]
            value = "-"
        elif match in OPERADORES:
            token_type = OPERADORES[match]
            value = "-"
        elif match in OPERADORES_RELACIONAIS:
            token_type = OPERADORES_RELACIONAIS[match]
            value = "-"
        elif match in OPERADORES_LOGICOS:
            token_type = OPERADORES_LOGICOS[match]
            value = "-"
        elif match in BITWISE_OPERATORS:
            token_type = BITWISE_OPERATORS[match]
            value = "-"
        elif match in SIMBOLOS_ESPECIAIS:
            token_type = SIMBOLOS_ESPECIAIS[match]
            value = "-"
        elif match.isdigit():
            token_type = "NUMBER"
            value = match
        else:
            token_type = "ID"
            value = "-"
        
        tokens.append((token_id, match, token_type, value)) #adiciona o token à lista de tokens
        tokenized_array.append(f"<{token_type}, {token_id}>") #adiciona o token formatado ao array tokenizado
        token_id += 1 #incrementa o identificador do token para continuar o laço
    
    return tokens, tokenized_array #retorna a lista de tokens e o array tokenizado

#codigo para análise léxica
code = """
int a = 134;
int b = c23;
if(b > 30)
    int c = b + a;
if(a > 100) {
    int c = a - b;
    int d = a * a + c;
}
"""

#tokeniza o código
tokens, tokenized_array = tokenize(code)

#cria um DataFrame para exibir a tabela de símbolos
df = pd.DataFrame(tokens, columns=["id", "lexema", "token", "valor"])
print(df) #imprimir tabela

#exibe a versão tokenizada do código
tokenized_output = " ".join(tokenized_array)
print("Código Tokenizado:", tokenized_output) #imprime o código tokenizado